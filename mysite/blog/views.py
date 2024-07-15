from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def test1(request):
    return HttpResponse("blog/test1 응답")

def test2(request, no):
    print("no type : ", type(no))
    return HttpResponse(f"no:{no}")

def test3(request, year, month, day):
    return HttpResponse(f"년:{year} 월:{month} 일:{day}")