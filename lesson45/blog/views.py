from asgiref.sync import sync_to_async, async_to_sync
from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.views import View
from django.views.generic import ListView
from django.views.generic.edit import CreateView
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
# from django.http import HttpResponse


from .models import Post, Tag
from .forms import PostForm, TagForm, LoginUserForm, RegisterUserForm

# Create your views here.

# @login_required(login_url='login/')
def home_blog(request):
    return render(request, "blog/base_blog.html")
    # if request.method == 'GET':
    #     posts = Post.objects.all()
    #     print(request.method)
    #     # posts_list = []
    #     # for post in posts:
    #     #     posts_list.append(f"{post.title:20}: {post.slug:20}")
    #     # print(f"<Blog homopage\n{'\n'.join(posts_list)}>")
    #     # result = f"<p>{'<br>'.join(posts_list)}</p>"
    #     # return HttpResponse("<h2>Blog homopage</h2>" + result)
    #     return render(request, "blog/posts.html", {'posts': posts})
    # else:
    #     pass


# class Posts(View):
#     def get(self, request):
#         posts = Post.objects.all()
#         return render(request, "blog/posts.html", {'posts': posts})
    

class Posts(View):
    async def get(self, request):
        posts = await sync_to_async(Post.objects.all)()
        return await sync_to_async(render)(request, "blog/posts.html", {'posts': posts})
    
    # def post(self, request):
    #     return render(request, "blog/posts.html")


# class Posts(ListView):
#     model = Post
#     template_name = "blog/posts.html"  
#     context_object_name = 'posts'
    # extra_context = {

    # }
    #  Post.objects.all()
    # def get_queryset(self):
    #     return Post.objects.all().filter()
    
    # def get_context_data(self):  # /?par=value
    #     context = super().get_context_data()
    #     context['title'] = "Post list"
    #     context.get() = self.request.GET.get('key', '')
    #     return context


class Tags(View):
    def get(self, request):
        tags = Tag.objects.all()
        return render(request, "blog/tags.html", {'tags': tags})
    
# class Tags(View):
#     async def get(self, request):
#         tags = Tag.objects.all()
#         return await sync_to_async(render)(request, "blog/tags.html", {'tags': tags})
    

# class PostDetail(View):  # DetailView
#     def get(self, request, slug):
#         post = Post.objects.get(slug=slug)
#         return render(request, "blog/post_detail.html", {'post': post}) 
    

class PostDetail(View):  # DetailView
    async def get(self, request, slug):
        post = await Post.objects.aget(slug=slug)
        return await sync_to_async(render)(request, "blog/post_detail.html", {'post': post}) 
    

class PostCreate(LoginRequiredMixin, View):
    # login_url = "login/"
    def get(self, request):
        form = PostForm()
        return render(request, "blog/post_create.html", {'post': form})
    
    def post(self, request):
        # post = Post.objects.create(
        #     title=request.POST['title'],
        #     slug=request.POST['slug'],
        #     body=request.POST['body']
        # )
        bound_form = PostForm(request.POST)
        if bound_form.is_valid():
            post = bound_form.save()
            # return  render(request, "blog/post_detail.html", {'post': post})
            return redirect('post_detail_url', post.slug)
        return  render(request, "blog/post_create.html", {'post': bound_form})
    

class PostUpdate(LoginRequiredMixin, View):
    # login_url = "login/"
    def get(self, request, slug):
        post = Post.objects.get(slug__iexact=slug)
        form = PostForm(instance=post)
        return render(request, "blog/post_update.html", {'form': form, 'post': post})
    
    def post(self, request, slug):
        post = Post.objects.get(slug__iexact=slug)
        bound_form = PostForm(request.POST, instance=post)
        if bound_form.is_valid():
            new_post = bound_form.save()
            return redirect(new_post)
        return render(request, "blog/post_update.html", {'form': bound_form, 'post': post})
    

class PostDelete(LoginRequiredMixin, View):
    login_url = "home_blog_url"
    # redirect_field_name = 'login'
    # raise_exception = True

    def get(self, request, slug):
        post = Post.objects.get(slug__iexact=slug)
        form = PostForm(instance=post)
        return render(request, "blog/post_delete.html", {'form': form, 'post': post})
    
    def post(self, request, slug):
        post = Post.objects.get(slug__iexact=slug)
        post.delete()
        return redirect('posts_list_url')
    

class TagCreate(View):
    def get(self, request):
        form = TagForm()
        return render(request, "blog/tag_create.html", {'tag': form})
    
    def post(self, request):
        bound_form = TagForm(request.POST)
        if bound_form.is_valid():
            tag = bound_form.save()
            # return  render(request, "blog/tag_detail.html", {'tag': tag})
            return redirect('tag_detail_url', tag.slug)
        return  render(request, "blog/tag_create.html", {'tag': bound_form})
    

class TagUpdate(LoginRequiredMixin, View):
    # login_url = "blog/login/"
    def get(self, request, slug):
        tag = Tag.objects.get(slug__iexact=slug)
        form = TagForm(instance=tag)
        return render(request, "blog/tag_update.html", {'form': form, 'tag': tag})
    
    def post(self, request, slug):
        tag = Tag.objects.get(slug__iexact=slug)
        bound_form = TagForm(request.POST, instance=tag)
        if bound_form.is_valid():
            new_tag = bound_form.save()
            return redirect(new_tag)
        return render(request, "blog/tag_update.html", {'form': bound_form, 'tag': tag})


class TagDelete(View):
    def get(self, request, slug):
        tag = Tag.objects.get(slug__iexact=slug)
        form = TagForm(instance=tag)
        return render(request, "blog/tag_delete.html", {'form': form, 'tag': tag})
    
    def post(self, request, slug):
        tag = Tag.objects.get(slug__iexact=slug)
        tag.delete()
        return redirect('posts_list_url')


class TagDetail(View):
    def get(self, request, slug):
        tag = Tag.objects.get(slug=slug)
        return render(request, "blog/tag_detail.html", {'tag': tag}) 
    

def login_user(request):
    if request.method == 'POST':
        form = LoginUserForm(request.POST)
        if form.is_valid():
            user = authenticate(
                request, 
                username=form.cleaned_data['username'], 
                password=form.cleaned_data['password']
            )
            if user and user.is_active:
                login(request, user)
                return redirect('home_blog_url')
    else:
        form = LoginUserForm()
    return render(request, "blog/login.html", {'form': form})

def logout_user(request):
    logout(request)
    return redirect('home_blog_url')


# def register(request):
#     if request.method == 'POST':
#         form = RegisterUserForm(request.POST)
#         if form.is_valid():
#             user = form.save(commit=False)
#             user.set_password(form.cleaned_data['password'])
#             user.save()
#             return redirect('home_blog_url')
#     else:
#         form = RegisterUserForm()
#     return render(request, 'blog/register.html', {'form': form})

class RegisterUser(CreateView):
    form_class = RegisterUserForm
    template_name = 'blog/register.html'
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('home_blog_url')