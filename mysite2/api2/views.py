from django.contrib.auth.models import User
from rest_framework import viewsets
from .serializers import *
from blog.models import Post, Comment
from rest_framework.generics import *
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.pagination import PageNumberPagination
from collections import OrderedDict

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
class PostPageNumberPagination(PageNumberPagination):
    page_size = 3
    def get_paginated_response(self, data):
        return Response(OrderedDict([
            ('pageCnt', self.page.paginator.num_pages),
            ('curPage', self.page.number),
            ('postList', data),
        ]))
    
class PostListAPIView(ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostListSerializer
    pagination_class = PostPageNumberPagination
    def get_serializer_context(self):
        return {
            'request' : None,
            'format' : self.format_kwarg,
            'view' : self
        }
    
class PostRetrieveAPIView(RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializerDetail
    
    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        prevInstance, nextInstance = get_prev_next(instance)
        commentList = instance.comment_set.all()
        data = {
            'post':instance,
            'prevPost':prevInstance,
            'nextPost':nextInstance,
            'commentList':commentList
        }
        serializer = self.get_serializer(instance=data)
        
        return Response(serializer.data)

    def get_serializer_context(self):
        return {
            'request':None,
            'format':self.format_kwarg,
            'view':self
        }
    
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
        return Response(data['like'])
    
class CateTagAPIView(APIView):
    def get(self, request, *args, **kwargs):
        cateList = Category.objects.all()
        tagList = Tag.objects.all()
        data = {
            'cateList' : cateList,
            'tagList' : tagList
        }
        serializer = CateTagSerializer(instance=data)
        return Response(serializer.data)
    
class PostLikeAPIView(GenericAPIView):
    queryset = Post.objects.all()
    def get(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.like += 1
        instance.save()
        return Response(instance.like)

def get_prev_next(instance):
    try:
        prev = instance.get_previous_by_update_dt()
    except instance.DoesNotExist:
        prev = None
    
    try:
        next_ = instance.get_next_by_update_dt()
    except instance.DoseNotExist:
        next_ = None
    
    return prev, next_
        