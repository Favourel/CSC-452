from django.urls import path, re_path
from . import views as user_views

urlpatterns = [
    path('update-profile/', user_views.update_profile, name='update_profile'),

    path("notification/", user_views.notification_view, name="notification"),

    # path("<slug:username>/follow/", user_views.follower_view, name="follow"),
    re_path(r'^(?P<username>.+)/follow/$', user_views.follower_view, name='follow'),
    re_path(r'^(?P<username>.+)/post/$', user_views.profile_view, name='a_follower_post_view'),

    path(r'^api/(?P<username>[^/]+)/follow/$', user_views.UserFollowerApi.as_view(), name='follower-api'),
    path(r'^api/(?P<username>[^/]+)/post_notify/$', user_views.PostNotificationApi.as_view(), name='post_notify'),
    path(r'^api/(?P<username>[^/]+)/mute_profile/$', user_views.MuteProfileApi.as_view(), name='mute_profile'),
    path(r'^api/(?P<username>[^/]+)/block_user/$', user_views.BlockProfileApi.as_view(), name='block_user'),

    # path('api/<slug:username>/follow/', user_views.UserFollowerApi.as_view(), name='follower-api'),
    # path('api/<slug:username>/post_notify/', user_views.PostNotificationApi.as_view(), name='post_notify'),
    # path('api/<slug:username>/mute_profile/', user_views.MuteProfileApi.as_view(), name='mute_profile'),
    # path('api/<slug:username>/block_user/', user_views.BlockProfileApi.as_view(), name='block_user'),


]