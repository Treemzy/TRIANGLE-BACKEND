# Generated by Django 4.1 on 2022-09-30 22:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0004_remove_post_comments_post_category_post_commets'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='commets',
        ),
        migrations.RemoveField(
            model_name='post',
            name='likes',
        ),
    ]
