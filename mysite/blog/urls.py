from django.urls import path
from . import views

urlpatterns = [
    path('test1/', views.test1),
    path('test2/<int:no>', views.test2),
    path('test3/<year>/<month>/<day>/', views.test3)
]

