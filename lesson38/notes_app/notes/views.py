from django.http import HttpResponse

def hello_notes(request):
    return HttpResponse("<h1>Hello from Notes app.</h1>")