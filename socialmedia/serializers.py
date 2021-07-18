from rest_framework import serializers
from base.serializers import UserSerializer
from .models import Post, Comment, Story, Tag

class PostSerializer(serializers.ModelSerializer):
    author = serializers.SerializerMethodField(read_only=True)
    tags = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Post
        fields = '__all__'

    def get_author(self, obj):
        author = obj.author
        serializer = UserSerializer(author, many=False)
        return serializer.data

    def get_tags(self, obj):
        tags = obj.tags.all()
        serializer = TagSerializer(tags, many=True)
        return serializer.data


class CommentSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Comment
        fields = '__all__'

    def get_user(self, obj):
        user = obj.user
        serializer = UserSerializer(user, many=False)
        return serializer.data


class StorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Story
        fields = '__all__'


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'