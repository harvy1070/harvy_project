from django.contrib import admin
from .models import *


# Register your models here.
# admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(User)
admin.site.register(Profile)
admin.site.register(Tag)

class PostAdmin(admin.ModelAdmin):
    pass

admin.site.register(Post, PostAdmin)