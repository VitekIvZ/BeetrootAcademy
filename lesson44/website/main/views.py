from django.shortcuts import render, redirect, get_object_or_404
from .forms import RegisterForm, PostForm, GroupForm
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User, Group
from django.core.exceptions import PermissionDenied
from .models import Post, MyGroup

"""
@login_required(login_url='/login')
def home(request):
    # Фільтруємо пости, щоб показувати лише ті, які належать поточному користувачу
    posts = Post.objects.filter(author=request.user)
    
    if request.method == 'POST':
        post_id = request.POST.get('post-id')
        user_id = request.POST.get('user-id')
        
        if post_id:
            post = get_object_or_404(Post, id=post_id)
            # Перевіряємо, чи поточний користувач є автором поста
            if post.author == request.user:
                post.delete()
        elif user_id:
            user = User.objects.filter(id=user_id).first()
            if user and request.user.is_staff:
                try:
                    group = Group.objects.get(name='default')
                    group.user_set.remove(user)
                except:
                    pass
                try:
                    group = Group.objects.get(name='mod')
                    group.user_set.remove(user)
                except:
                    pass
    
    return render(request, 'main/home.html', {'posts': posts})
"""

@login_required(login_url='/login')
def home(request):
    # Отримуємо параметр "type" з GET-запиту (за замовчуванням - 'personal')
    post_type = request.GET.get('type', 'personal')
    
    if post_type == 'group':
        # Отримуємо пости груп, до яких належить користувач
        #groups = request.user.groups.all()  # Отримуємо групи користувача
        groups = MyGroup.objects.filter(members=request.user)
        posts = Post.objects.filter(group__in=groups)  # Фільтруємо пости за групами
    else:
        # Отримуємо персональні пости користувача
        posts = Post.objects.filter(author=request.user, group__isnull=True)
    
    return render(request, 'main/home.html', {'posts': posts, 'post_type': post_type})

@login_required(login_url='/login')
def create_group(request):
    if request.method == 'POST':
        form = GroupForm(request.POST)
        if form.is_valid():
            group = form.save()
            group.members.add(request.user)  # Додаємо поточного користувача до групи
            return redirect('group-detail', group_id=group.id)
    else:
        form = GroupForm()
    return render(request, 'main/create_group.html', {'form': form})

@login_required(login_url='/login')
def group_detail(request, group_id):
    group = get_object_or_404(MyGroup, id=group_id)
    posts = group.posts.all()  # Отримуємо всі пости групи
    #return render(request, 'main/group_detail.html', {'group': group, 'posts': posts})
    return render(request, 'main/group_detail.html', {'group': group, 'posts': posts, 'group_id': group.id })

@login_required(login_url='/login')
@permission_required('main.add_post', login_url='/login')
def create_post(request, group_id):
    group = get_object_or_404(MyGroup, id=group_id)
    
    # Перевіряємо, чи поточний користувач є членом групи
    if request.user not in group.members.all():
        raise PermissionDenied("You are not a member of this group.")
    
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.group = group
            post.save()
            return redirect('group-detail', group_id=group.id)
    else:
        form = PostForm()
    return render(request, 'main/create_post.html', {'form': form, 'group': group})

@login_required(login_url='/login')
@permission_required('main.add_post', login_url='/login')
def create_group_post(request, group_id):
    group = get_object_or_404(MyGroup, id=group_id)
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.group = group
            post.save()
            return redirect('group-detail', group_id=group.id)
    else:
        form = PostForm()
    return render(request, 'main/create_post.html', {'form': form, 'group_id': group_id})


@login_required(login_url='/login')
def post_detail(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    return render(request, 'main/post_detail.html', {'post': post})


@login_required(login_url='/login')
def update_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    
    # Перевіряємо, чи поточний користувач є автором поста
    if post.author != request.user:
        return redirect('/home')  # Або повернути помилку 403
    
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('/home')
    else:
        form = PostForm(instance=post)
    
    return render(request, 'main/update_post.html', {'form': form})


@login_required(login_url='/login')
def delete_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    
    # Перевіряємо, чи поточний користувач є автором поста
    if post.author != request.user:
        return redirect('/home')  # Або повернути помилку 403
    
    if request.method == 'POST':
        post.delete()
        return redirect('/home')
    
    return render(request, 'main/confirm_delete.html', {'post': post})

def ban_user(request, user_id):
    user = get_object_or_404(User, id=user_id)
    if request.method == 'POST':
        user.is_active = False
        user.save()
        return redirect('home')
    return render(request, 'registration/ban_user_confirm.html', {'user': user})

def sign_up(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/home')
    else:
        form = RegisterForm()
    
    return render(request, 'registration/sign_up.html', {'form': form})

def group_list(request):
    groups = MyGroup.objects.all()  # Отримуємо всі групи
    return render(request, 'main/group_list.html', {'groups': groups})


def logout_view(request):
    logout(request)
    return redirect('/home')
    
