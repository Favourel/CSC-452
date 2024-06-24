from django.urls import path
from . import views as feed_view

urlpatterns = [
    path('feed/', feed_view.post_list_view, name='feed_home'),
    path('post/<int:pk>/', feed_view.post_detail_view, name='post_detail_view'),
    path('repost/<int:pk>/', feed_view.post_detail_view, name='repost_detail_view'),
    path('comment/<int:pk>/', feed_view.post_comment, name='post_comment'),
    path('repost/comment/<int:pk>/', feed_view.repost_comment, name='repost_comment'),
    path('repost/<int:pk>/add/', feed_view.repost_add_view, name='repost_add_view'),
    path('repost-/<int:pk>/add/', feed_view.repost_add_view_, name='repost_add_view-'),
    path('search/', feed_view.search, name='search'),
    path('api/<int:pk>/add/', feed_view.PostLikeApi.as_view(), name='like-api'),
    path('repost/<int:pk>/add_like/', feed_view.RepostLikeApi.as_view(), name='repost_like-api'),
    path('create_post/', feed_view.create_post, name='create_post'),
    # path('blog/<int:pk>/update/', blog_view.PostUpdateView.as_view(), name='post_detail_view'),
    path('post/<int:pk>/delete/', feed_view.PostDeleteView.as_view(), name='post_delete_view'),

    path('form/', feed_view.ajax_posting, name="join"),

    path('push_feed/', feed_view.push_feed, name="push_feed"),

]