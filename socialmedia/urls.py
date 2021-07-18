from django.urls import path
from .views import (
    followed_user_posts, detail_post,
    like_post, follow_user,
    comment_create, comment_edit,
    comment_delete, post_create,
    user_search, story_create,
    story_delete, get_story_users,
    post_comments, comment_detail,
    getUserById, isFollowed,
    user_posts, uploadImage
)

urlpatterns = [
    path('', followed_user_posts, name=""),
    path('search_user/', user_search, name=""),
    path('posts/<int:pk>/', detail_post, name=""),
    path('posts/create/', post_create, name=""),
    path('posts/like/<int:pk>/', like_post, name=""),
    path('follow/<int:pk>/', follow_user, name=""),
    path('posts/<int:pk>/comments/', post_comments, name=""),
    path('posts/<int:pk>/comment/', comment_create, name=""),
    path('posts/comment/<int:pk>/', comment_detail, name=""),
    path('posts/comment/<int:pk>/edit/', comment_edit, name=""),
    path('posts/comment/<int:pk>/delete/', comment_delete, name=""),
    path('story/create/', story_create, name=""),
    path('story/<int:pk>/delete/', story_delete, name=""),
    path('user_stories/', get_story_users, name=""),
    path('users/<int:pk>/', getUserById, name=""),
    path('is_followed/<int:pk>/', isFollowed, name=""),
    path('users/<int:pk>/posts/', user_posts, name=""),
    path('posts/<int:pk>/upload/', uploadImage, name=""),
]