from rest_framework import serializers
from insta_clone.posts.models import Post, Comment
from insta_clone.users.api.serializers import UserSerializer


class CommentSerializer(serializers.ModelSerializer):
    replies = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Comment
        fields = ['id', 'post', 'parent_comment', 'description', 'likes', 'replies']


class PostSerializer(serializers.ModelSerializer):
    likes = serializers.IntegerField(source='likes', read_only=True)
    users_whom_liked = UserSerializer(many=True, read_only=True)
    comments = CommentSerializer(many=True, read_only=True)

    class Meta:
        model = Post
        fields = ['id', 'resource_url', 'description', 'location', 'likes', 'users_whom_liked', 'comments']
