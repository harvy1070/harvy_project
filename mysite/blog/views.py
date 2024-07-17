from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from .models import Post, User, Tag
from django.utils import timezone
from .forms import PostForm

# TEST LIST
def test1(request):
    return HttpResponse("blog/test1 응답")

def test2(request, no):
    print("no type : ", type(no))
    return HttpResponse(f"no:{no}")

def test3(request, year, month, day):
    return HttpResponse(f"년:{year} 월:{month} 일:{day}")

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

def test6(request):
    d1 = timezone.now()
    d2 = timezone.datetime(2001,3,19)
    d3 = timezone.datetime(2030,3,19)
    
    return render(request, 'blog/test6.html', {'date1':d1, 'date2':d2, 'date3':d3})

def test7(request):
    print('요청방식 : ', request.method)
    print('GET 방식 : ', request.GET)
    print('POST 방식 : ', request.POST)
    print('업로드 파일 : ', request.FILES)
    
    return render(request, 'blog/form_test.html')

# PAGE LIST
def list(request):
    post_list = Post.objects.all()
    search_key = request.GET.get("keyword")
    if search_key:
        post_list = Post.objects.filter(title__icontains=search_key)
    return render(request, 'blog/list.html', {'post_list':post_list, 'q':search_key})

def detail(request, id):
    post = get_object_or_404(Post, id=id)
    comment_all = post.comments.all()
    tag_list = post.tag.all()
    return render(request, 'blog/detail.html', {'post':post, 'comment_all':comment_all, 'tag_list':tag_list})

def profile(request):
    user = User.objects.get(id=1)
    return render(request, 'blog/profile.html', {'user':user})

def tag_list(request, id):
    tag = Tag.objects.get(id=id)
    post_list = tag.post_set.all()
    return render(request, 'blog/list.html', {'post_all':post_list})

def post_create(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            # 딕셔너리 언패킹
            Post.objects.create(**form.cleaned_data)
            return HttpResponse("추가 작업 완료")
    else:
        form = PostForm()
        return render(request, 'blog/post_form.html', {'form':form})