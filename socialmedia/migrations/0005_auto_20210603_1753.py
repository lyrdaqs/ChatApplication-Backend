# Generated by Django 3.2 on 2021-06-03 13:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('socialmedia', '0004_post_tag'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserLikedPost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('likedPost', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='likers', to='socialmedia.post')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='likedPosts', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddConstraint(
            model_name='userlikedpost',
            constraint=models.UniqueConstraint(fields=('user', 'likedPost'), name='unique_liked_post'),
        ),
    ]
