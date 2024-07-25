from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from django.views.generic import TemplateView

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('signup/', views.signup, name='signup'),
    
    path(
        "password_change/", auth_views.PasswordChangeView.as_view(), name="password_change"
    ),
    path(
        "password_change/done/",
        auth_views.PasswordResetDoneView.as_view(),
        name="password_change_done",
    ),
    path('profile/', TemplateView.as_view(template_name='registration/profile.html'), name='profile'),
]