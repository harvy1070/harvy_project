from django.urls import path
from . import views

app_name='blog'

urlpatterns = [
    # Test
    path('test1/', views.test1),
    path('test2/<int:no>', views.test2),
    path('test3/<year>/<month>/<day>/', views.test3),
    path('test4/', views.test4),
    path('test5/', views.test5),
    path('test6/', views.test6),
    path('test7/', views.test7),
    
    # Page List
    path('', views.list, name='list'),
    path('<int:id>/', views.detail, name='detail'),
    path('profile/', views.profile),
    path('tag/<id>', views.tag_list),
    path('new/', views.post_create, name='create'),
    path('update/<id>', views.post_update, name='update'),
    path('delete/<id>', views.post_delete, name='delete'),
]

