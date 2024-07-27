from django.contrib.auth.models import User
from rest_framework import viewsets
from .serializers import UserSerializer, PostSerializer, CommentSerializer
from blog.models import Post, Comment
from rest_framework.generics import *
from .serializers import *
from rest_framework.response import Response

# Router을 활용한 Path 정의
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    
class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    
class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    
# URL Path 직접 정의
class PostListAPIView(ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostListSerializer
    
class PostRetrieveAPIView(RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostRetrieveSerializer
    
class CommentCreateAPIView(CreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    
class PostLikeAPIView(UpdateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostListSerializer
    
    def update(self, request, *args, **kwargs):
        # 부분 업데이트 허용 금지
        partial = kwargs.pop('partial', False)
        # 요청 객체 가져오기
        instance = self.get_object()
        # like 필드값 1 증가
        data = {'like':instance.like + 1}
        # 새 데이터와 결합
        serializer = self.get_serializer(instance, data=data, partial=partial)
        serializer.is_valid(raise_exception=True)
        # 객체 업데이트
        self.perform_update(serializer)
        
        # 미리 가져온 객체 캐시 지우기(일관성 유지)
        if getattr(instance, '_prefetched_objects_cache', None):
            instance._prefetched_objects_cache = {}
        return Response(serializer.data)
            