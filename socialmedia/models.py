from django.core.exceptions import ObjectDoesNotExist
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models import UniqueConstraint

class User(AbstractUser):
    phoneNumber = models.CharField(max_length=200, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    bio = models.TextField(null=True, blank=True, default='')


class UserFollowing(models.Model):
    user = models.ForeignKey(User, related_name="following", on_delete=models.CASCADE)
    followingUser = models.ForeignKey(User, related_name="followers", on_delete=models.CASCADE)
    createdAt = models.DateTimeField(auto_now_add=True)

    class Meta:
        constraints = [
            UniqueConstraint(
                fields=['user', 'followingUser'], name="unique_followers"
            )
        ]

    def __str__(self):
        return f'{self.user.first_name} follow {self.followingUser.first_name}'


class Tag(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Post(models.Model):
    image = models.ImageField()
    caption = models.TextField()
    author = models.ForeignKey(User, related_name="posts", on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag, related_name='posts')

    def __str__(self):
        return f'{self.author.first_name} posted'

    @staticmethod
    def addTag(tags, post):
        for t in tags:
            try:
                exist_tag = Tag.objects.get(name=t['name'])
                tag = exist_tag
            except ObjectDoesNotExist:
                tag = Tag.objects.create(name=t['name'])
            post.tags.add(tag)
        post.save()


class UserLikedPost(models.Model):
    user = models.ForeignKey(User, related_name="likedPosts", on_delete=models.CASCADE)
    likedPost = models.ForeignKey(Post, related_name="likers", on_delete=models.CASCADE)
    createdAt = models.DateTimeField(auto_now_add=True)

    class Meta:
        constraints = [
            UniqueConstraint(
                fields=['user', 'likedPost'], name="unique_liked_post"
            )
        ]

    def __str__(self):
        return f'{self.user.first_name} like {self.likedPost.id}'


class Comment(models.Model):
    user = models.ForeignKey(User, related_name="comments", on_delete=models.CASCADE)
    post = models.ForeignKey(Post, related_name="comments", on_delete=models.CASCADE)
    content = models.TextField()
    createdAt = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user.first_name} commented {self.post.id}'


class Story(models.Model):
    user = models.ForeignKey(User, related_name="stories", on_delete=models.CASCADE)
    image = models.ImageField()