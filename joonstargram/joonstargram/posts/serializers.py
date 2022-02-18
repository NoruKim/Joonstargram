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

    def create(self, validated_data):
        author_data = validated_data.pop('author')
        author = User.objects.create(**author_data)
        comment_data = validated_data.pop('comment_post')
        comment_post = Comment.objects.create(**comment_data)
        post = Post.objects.create(author=author, comment_post=comment_post, **validated_data)

        return post
