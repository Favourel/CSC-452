# Generated by Django 4.0.4 on 2024-06-23 15:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('feed', '0003_remove_postnotification_blog_and_more'),
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PostNotification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('notification_type', models.IntegerField(choices=[(1, 'Post Notification'), (2, 'Like Notification')])),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
                ('is_seen', models.BooleanField(default=False)),
                ('blog', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='feed.post')),
                ('repost_blog', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='feed.blogrepost')),
                ('sender', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='notification_from_user', to=settings.AUTH_USER_MODEL)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='notification_to_user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('notification_type', models.IntegerField(choices=[(1, 'likes'), (2, 'comment'), (3, 'follow'), (4, 'Repost'), (5, 'Liked_a_Repost'), (6, 'Commented_on_a_Repost'), (7, 'Post Notification'), (8, 'Repost of repost'), (9, 'Account Created')])),
                ('text_preview', models.CharField(blank=True, max_length=200, null=True)),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
                ('is_seen', models.BooleanField(default=False)),
                ('blog', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='feed.post')),
                ('notify_users', models.ManyToManyField(blank=True, related_name='notify_users', to=settings.AUTH_USER_MODEL)),
                ('repost_blog', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='feed.blogrepost')),
                ('sender', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='noti_from_user', to=settings.AUTH_USER_MODEL)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='noti_to_user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
