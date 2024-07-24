from django.contrib import admin
from .models import *


# Register your models here.
# admin.site.register(Post)
# admin.site.register(Comment)
admin.site.register(User)
admin.site.register(Profile)
admin.site.register(Tag)

class CommentInline(admin.TabularInline):
    model = Comment

# Post 관리자 페이지 커스터마이징
class PostAdmin(admin.ModelAdmin):
    # list 송출 항목
    list_display = ['id', 'title', 'body']
    # list link
    list_display_links = ['id', 'title']
    # 정렬 방식
    ordering = ['id']
    # filter 구분, tag 항목을 필터로 활용
    list_filter = ['tag']
    # 검색 필드, 검색 글자가 아래 항목에 해당되면 출력
    search_fields = ['id', 'title', 'body']
    # page 분할
    list_per_page = 3
    # 모델 필드 그룹화
    filedsets = (
        ('기본정보', {'fields':('title', 'body')}),
        ('기타정보', {'fields':('tag', 'ip')}),
    )
    # 관리자 페이지 인라인 표기
    inlines = (CommentInline,)

admin.site.register(Post, PostAdmin)


# Comment 관리자 커스터마이징
def make_deleted(modeladmin, request, queryset):
    queryset.update(deleted=True)

make_deleted.short_description = '선택된 댓글을 삭제상태로 설정'

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['post', 'author', 'message_length', 'deleted']
    actions = [make_deleted]
    def message_length(self, obj):
        return len(obj.message)
    message_length.short_description = '댓글 글자 수'