from django.contrib import admin
from socialmedia.models import *
from django.contrib.auth.admin import UserAdmin

admin.site.register(User, UserAdmin)
admin.site.register(UserFollowing)
admin.site.register(Post)
admin.site.register(Tag)
admin.site.register(UserLikedPost)
admin.site.register(Story)
admin.site.register(Comment)

