from django.utils import timezone

from django.db import models
from django.contrib.auth.models import AbstractUser
from django.shortcuts import reverse
from django.conf import settings

from feed.models import BlogRepost, Post
from django.core.validators import RegexValidator
from django.utils.translation import gettext_lazy as _

username_validator = RegexValidator(
    regex=r'^[@\w.+-]{1,150}$',  # Allow letters, numbers, and specific special characters
    message='Username must consist of letters, numbers, or @/./+/-/_ characters.',
    code='invalid_username'
)
# Create your models here.


class User(AbstractUser):
    # username = models.CharField(_('username'), max_length=150, unique=True, validators=[username_validator])

    username = models.CharField(
        max_length=150,
        unique=True,
        validators=[
            RegexValidator(
                regex=r'^[\w@./+-]+$',  # Adjust the regex to include other characters if needed
                message="Username must consist of letters, numbers, or @/./+/-/_ characters."
            ),
        ],
        error_messages={
            'unique': "A user with that username already exists.",
        },
    )

    display_name = models.CharField(max_length=20, null=True, blank=True)
    about = models.CharField(max_length=255, null=True, blank=True)
    image = models.ImageField(default='profile.png', upload_to='profile_picture')

    follower = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True, related_name='follower_list')
    following = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True, related_name='following_list')

    background_image = models.ImageField(default="WIN_20220328_15_20_55_Pro.jpg", upload_to="profile_background_image")
    account_visit = models.IntegerField(default=0)
    account_engaged = models.IntegerField(default=0)
    has_viewed = models.BooleanField(default=False)
    is_verified = models.BooleanField(default=False)
    post_notification = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True, related_name='post_notify')
    mute_list = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True, related_name='mute')
    block_list = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True, related_name='block')

    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url

    def get_follower_api_url(self):
        return reverse('follower-api', kwargs={'username': self.username})

    def post_notify_api_url(self):
        return reverse('post_notify', kwargs={'username': self.username})


class UserStat(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, blank=True, on_delete=models.CASCADE)
    account_visit = models.IntegerField(default=0)
    account_engaged = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.user} stat"


class Story(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, blank=True, null=True, on_delete=models.CASCADE)
    story_image = models.ImageField(upload_to='story_picture', blank=True, null=True)

    def __str__(self):
        return f"{self.user} story"


class Notification(models.Model):
    NOTIFICATION_TYPES = (
        (1, "likes"), (2, "comment"), (3, "follow"),
        (4, "Repost"), (5, "Liked_a_Repost"), (6, "Commented_on_a_Repost"), (7, "Post Notification"),
        (8, "Repost of repost"), (9, "Account Created")
                          )

    user = models.ForeignKey(settings.AUTH_USER_MODEL, blank=True, null=True, on_delete=models.CASCADE,
                             related_name="noti_to_user")
    sender = models.ForeignKey(settings.AUTH_USER_MODEL, blank=True,
                               on_delete=models.CASCADE, related_name="noti_from_user")

    blog = models.ForeignKey(Post, null=True, blank=True, on_delete=models.CASCADE)
    repost_blog = models.ForeignKey(BlogRepost, null=True, blank=True, on_delete=models.CASCADE)
    # repost_of_repost = models.ForeignKey(BlogRepost.repost, null=True, blank=True, on_delete=models.CASCADE)
    notification_type = models.IntegerField(choices=NOTIFICATION_TYPES)
    text_preview = models.CharField(max_length=200, blank=True, null=True)
    notify_users = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True, related_name='notify_users')

    date = models.DateTimeField(default=timezone.now)
    is_seen = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.sender} notification'


class PostNotification(models.Model):
    NOTIFICATION_TYPES = (
         (1, "Post Notification"), (2, "Like Notification")
                          )
    user = models.ForeignKey(settings.AUTH_USER_MODEL, blank=True, null=True, on_delete=models.CASCADE,
                             related_name="notification_to_user")
    sender = models.ForeignKey(settings.AUTH_USER_MODEL, blank=True,
                               on_delete=models.CASCADE, related_name="notification_from_user")

    blog = models.ForeignKey(Post, null=True, blank=True, on_delete=models.CASCADE)
    repost_blog = models.ForeignKey(BlogRepost, null=True, blank=True, on_delete=models.CASCADE)
    # repost_of_repost = models.ForeignKey(BlogRepost.repost, null=True, blank=True, on_delete=models.CASCADE)
    notification_type = models.IntegerField(choices=NOTIFICATION_TYPES)

    date = models.DateTimeField(default=timezone.now)
    is_seen = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.sender} notification'