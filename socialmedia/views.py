
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from .models import (
    Post, UserLikedPost,
    User, UserFollowing,
    Comment, Tag,
    Story
)
from .serializers import PostSerializer, CommentSerializer, StorySerializer
from base.serializers import UserSerializer


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def followed_user_posts(request):
    user = request.user
    following = user.following.all()
    following_users = [u.followingUser for u in following]
    posts = Post.objects.filter(author__in=following_users)

    serializer = PostSerializer(posts, many=True)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def detail_post(request, pk):
    post = Post.objects.get(id=pk)
    serializer = PostSerializer(post, many=False)
    return Response(serializer.data)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def post_create(request):
    user = request.user
    tags = request.data['tags']
    post = Post.objects.create(
        author=user,
        caption=request.data['caption']
    )
    Post.addTag(tags, post)
    return Response({"created_post": post.id})


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def user_posts(request, pk):
    user = User.objects.get(id=pk)
    posts = Post.objects.filter(author=user)
    serializer = PostSerializer(posts, many=True)
    return Response(serializer.data)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def like_post(request, pk):
    user = request.user
    post = Post.objects.get(id=pk)
    try:
        UserLikedPost.objects.create(
            user=user,
            likedPost=post
        )
    except:
        UserLikedPost.objects.filter(
            user=user,
            likedPost=post
        ).delete()

    like_num = len(UserLikedPost.objects.filter(likedPost=post))
    return Response({"like_num": like_num})


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def follow_user(request, pk):
    user = request.user
    following_user = User.objects.get(id=pk)
    try:
        UserFollowing.objects.create(
            user=user,
            followingUser=following_user
        )
        return Response(True)

    except:
        UserFollowing.objects.filter(
            user=user,
            followingUser=following_user
        ).delete()
        return Response(False)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def isFollowed(request, pk):
    current_user = request.user
    required_user = User.objects.get(id=pk)
    followers = required_user.followers.all()
    followers_users = [u.user for u in followers]
    if current_user in followers_users:
        return Response(True)
    else:
        return Response(False)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def comment_create(request, pk):
    user = request.user
    post = Post.objects.get(id=pk)
    comment = Comment.objects.create(
        user=user,
        post=post,
        content=request.data['content']
    )
    serializer = CommentSerializer(comment, many=False)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def post_comments(request, pk):
    post = Post.objects.get(id=pk)
    comments = Comment.objects.filter(post=post)
    serializer = CommentSerializer(comments, many=True)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def comment_detail(request, pk):
    comment = Comment.objects.get(id=pk)
    serializer = CommentSerializer(comment, many=False)
    return Response(serializer.data)


@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def comment_edit(request, pk):
    comment = Comment.objects.get(id=pk)
    comment.content = request.data['content']
    comment.save()
    serializer = CommentSerializer(comment, many=False)
    return Response(serializer.data)


@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def comment_delete(request, pk):
    comment = Comment.objects.get(id=pk)
    comment.delete()
    return Response("comment is deleted successfuly")


@api_view(['POST'])
def uploadImage(request, pk):
    post = Post.objects.get(id=pk)
    post.image = request.FILES.get('image')
    post.save()

    return Response('Image was uploaded')


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def uploadStory(request):
    data = request.data

    story_id = data['story_id']
    story = Story.objects.get(id=story_id)

    story.image = request.FILES.get('image')
    story.save()

    return Response('Image was uploaded')


@api_view(['GET'])
def user_search(request):
    query = request.query_params.get('keyword')
    if query:
        users = User.objects.filter(username__icontains=query)
    else:
        users = User.objects.none()

    serializer = UserSerializer(users, many=True)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getUserById(request, pk):
    user = User.objects.get(id=pk)
    serializer = UserSerializer(user, many=False)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def story_create(request):
    story = Story.objects.create(
        user=request.user,
        image=request.data['image']
    )
    serializer = StorySerializer(story, many=False)
    return Response(serializer.data)


@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def story_delete(request, pk):
    Story.objects.get(id=pk).delete()
    return Response("story deleted successfuly")


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_story_users(request):
    user = request.user
    following = user.following.all()
    following_users = [u.followingUser for u in following]
    stories = Story.objects.filter(user__in=following_users)

    serializer = StorySerializer(stories, many=True)
    return Response(serializer.data)