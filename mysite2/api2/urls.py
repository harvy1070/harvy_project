from django.urls import path, include
from rest_framework import routers
from .views import UserViewSet, PostViewSet, CommentViewSet
from . import views

# Router을 활용한 Path 정의
# router = routers.DefaultRouter()
# router.register('users', UserViewSet)
# router.register('post', PostViewSet)
# router.register('comment', CommentViewSet)

# URL Path 직접 정의
urlpatterns = [
    path('post/', views.PostListAPIView.as_view(), name="post-list"),
    path('post/<int:pk>/', views.PostRetrieveAPIView.as_view(), name="post-detail"),
    path('comment/', views.CommentCreateAPIView.as_view(), name="comment-list"),
    path('post/<int:pk>/like/', views.PostLikeAPIView.as_view(), name="post-like"),
    path('catetag/', views.CateTagAPIView.as_view(), name='catetag'),
]