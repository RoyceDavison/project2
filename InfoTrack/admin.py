from django.contrib import admin
# Register your models here.
from .models import User, Comment,Post
"""
class CommentInline(admin.TabularInline):
    model = Comment

class PostInline(admin.TabularInline):
    model = Post
"""

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    #inlines = [CommentInline]
    list_display = ("title",'context', 'time')

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    #inlines = [CommentInline]
    list_display = ('context', 'time')

@admin.register(User)
class Userdmin(admin.ModelAdmin):
    #inlines = [PostInline]
    list_display = ('username','time',"userid")



