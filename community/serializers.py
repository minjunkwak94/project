from rest_framework import serializers
from .models import Post, Comment

class PostSerializer(serializers.ModelSerializer):
  
    class Meta:
        model = Post
        fields = ('id', 'category', 'title', 'content', 'created_at', 'updated_at')

class CommentSerializer(serializers.ModelSerializer):
    # post = serializers.IntegerField(read_only=True)

    class Meta:
        model = Comment
        fields = ('id', 'post', 'content', 'created_at', 'updated_at')
        read_only_fields = ('post',)