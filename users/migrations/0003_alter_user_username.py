# Generated by Django 4.0.4 on 2024-06-23 16:27

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_postnotification_notification'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(max_length=150, unique=True, validators=[django.core.validators.RegexValidator(code='invalid_username', message='Username must consist of letters, numbers, or @/./+/-/_ characters.', regex='^[@\\w.+-]{1,150}$')], verbose_name='username'),
        ),
    ]