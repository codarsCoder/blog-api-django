# Generated by Django 4.1.4 on 2023-01-01 18:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_blog_b_user_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blog',
            old_name='b_user_id',
            new_name='user_id',
        ),
    ]