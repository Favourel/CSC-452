from django.contrib import admin
from .models import Story, UserStat, User, Notification, PostNotification


# Register your models here.


class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'date_joined')
    search_fields = ('username', 'email')


class UserStatAdmin(admin.ModelAdmin):
    list_display = ("user", "account_visit", "account_engaged")
    search_fields = ['user']


class NotificationAdmin(admin.ModelAdmin):
    list_display = ["sender", "notification_type", "user", "is_seen"]
    search_fields = ('sender', 'user')


class PostNotificationAdmin(admin.ModelAdmin):
    list_display = ["sender", "notification_type", "user", "is_seen"]
    search_fields = ('sender', 'user')


admin.site.register(User, UserAdmin)
admin.site.register(Story)
admin.site.register(UserStat, UserStatAdmin)
admin.site.register(Notification, NotificationAdmin)
admin.site.register(PostNotification, PostNotificationAdmin)
