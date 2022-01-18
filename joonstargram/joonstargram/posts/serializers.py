from rest_framework import serializers

from joonstargram.users.models import User
from .models import *

class PostAuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            "id",
            "username",
            "profile_photo",
            "intro",
            "followers",
            "followings",
        )

class CommentSerializer(serializers.ModelSerializer):
    author = PostAuthorSerializer()

    class Meta:
        model = Comment
        fields = (
            "id",
            "content",
            "author",
        )

class PostSerializer(serializers.ModelSerializer):
    comment_post = CommentSerializer(many=True)
    author = PostAuthorSerializer()

    class Meta:
        model = Post
        fields = (
            "id",
            "image",
            "caption",
            "comment_post",
            "author",
            "image_likes",
        )
