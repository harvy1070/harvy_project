from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
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
    return render(request, 'blog/list.html', {'post_list':post_list})

def detail(request, id):
    post = get_object_or_404(Post, id=id)
    return render(request, 'blog/detail.html', {'post':post})

def test4(request):
    return render(request, 'blog/test4.html', {'score':70})

def test5(request):
    var = '''
          Miracles happen to only those who believe in them.
          Think like a man of action and act like man of thought.
          Courage is very important. Like a muscle, it is strengthened by use.
          Life is the art of drawing sufficient conclusions from insufficient premises.
          By doubting we come at the truth.
          A man that has no virtue in himself, ever envies virtue in others.
          When money speaks, the truth keeps silent.
          Better the last smile than the first laughter.
          '''
    
    return render(request, 'blog/test5.html', {'var':var})