from rest_framework import serializers
from .models import Post, Comment

# class CommentSerializer(serializers.ModelSerializer):

#     class Meta:
#         model = Comment
#         fields = ('id', 'post', 'content', 'created_at', 'updated_at')
#         read_only_fields = ('post',)

# class PostSerializer(serializers.ModelSerializer):

#     comment_set = CommentSerializer(many=True, read_only=True)
#     class Meta:
#         model = Post
#         fields = ('id', 'category', 'title', 'content', 'created_at', 'updated_at', 'comment_set')


class CommentListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = ('id', 'content',)
        read_only_fields = ('post',)


class CommentDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = ('id', 'post', 'content', 'created_at', 'updated_at')


class PostListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = ('id', 'category', 'title', )


class PostDetailSerializer(serializers.ModelSerializer):

    comment_set = CommentListSerializer(many=True, read_only=True)
    class Meta:
        model = Post
        fields = ('id', 'category', 'title', 'content', 'created_at', 'updated_at', 'comment_set')