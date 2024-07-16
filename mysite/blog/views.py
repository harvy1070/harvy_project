from django.shortcuts import render
from django.http import HttpResponse
from .models import Post

# Create your views here.
def test1(request):
    return HttpResponse("blog/test1 응답")

def test2(request, no):
    print("no type : ", type(no))
    return HttpResponse(f"no:{no}")

def test3(request, year, month, day):
    return HttpResponse(f"년:{year} 월:{month} 일:{day}")

def list(request):
    post_list = Post.objects.all()
    titles = ""
    for post in post_list:
        titles += post.title
        
    return HttpResponse(titles)

def detail(request, id):
    post = Post.objects.get(id=id)
    return HttpResponse(post.title)