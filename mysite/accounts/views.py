from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.conf import settings
from .forms import SignupForm
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy
from django.contrib import messages

# Login
def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(settings.LOGIN_URL)
    else:form = SignupForm()
    
    return render(request, 'registration/signup.html', {'form':form})

# PasswordChange
class MypasswordChangeView(PasswordChangeView):
    success_url = reverse_lazy('profile')
    
    def form_valid(self, form):
        messages.info(self.request, '암호 변경 완료')
        return super().form_valid(form)
    
    
# Cookie Test View
def cookie_test(request, code):
    # 객체 응답 생성
    response = render(request, 'registration/cookieTest.html')
    # add 처리
    if code == 'add':
        # model에 A001 값 부여
        response.set_cookie('model', 'A001')
        # prod에 EV9 값 부여
        response.set_cookie('prod', 'EV9')
    # get 처리
    elif code == 'get':
        # model, prod 쿠키값을 가져옴
        model = request.COOKIES.get('model')
        prod = request.COOKIES.get('prod')
        print(model, prod)
    # del 처리
    elif code == 'del':
        # 쿠키 삭제
        response.delete_cookie('model')
        response.delete_cookie('prod')
    # 최종적 응답 객체 반환
    return response

# Session Test View
from django.contrib.sessions.backends.db import SessionStore

def session_test(request, code):
    response = render(request, 'registration/sessionTest.html')
    session = request.session
    if code == 1:
        user = request.user
        print(user,':',session)
    elif code == 2:
        session['model'] = 'A001'
        session['prod'] = 'EV9'
        print('Session 데이터 등록')
    elif code == 3:
        model = session.get('model')
        prod = session.get('prod')
        print('Session 데이터 추출')
        print(model, prod)
    elif code == 4:
        session.pop('model')
        print('Session 데이터 삭제')
        session.pop('prod')
    return response
