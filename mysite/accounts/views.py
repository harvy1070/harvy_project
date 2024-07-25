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