from django.contrib import admin
from .models import *

# Register your models here.


class CommentInline(admin.TabularInline):
    model = BlogComment


class RepostCommentInline(admin.TabularInline):
    model = BlogRepost


class PostAdmin(admin.ModelAdmin):
    list_display = ['content', 'author', 'date_posted']
    search_fields = ["content"]
    filter_horizontal = ['like']
    list_filter = ['author', 'date_posted']
    list_per_page = 10
    inlines = [CommentInline]


class BlogCommentAdmin(admin.ModelAdmin):
    list_display = ['user', "post", 'date_posted']


class BlogRepostAdmin(admin.ModelAdmin):
    list_display = ['user', "post", "repost", 'date_posted']
    inlines = [RepostCommentInline]


class BlogImagesAdmin(admin.ModelAdmin):
    list_display = ["post", "image", "date_posted"]


admin.site.register(Post, PostAdmin)
admin.site.register(BlogComment, BlogCommentAdmin)

admin.site.register(BlogRepost, BlogRepostAdmin)
admin.site.register(RepostComment)
admin.site.register(BlogImages, BlogImagesAdmin)
admin.site.register(RecentSearch)
