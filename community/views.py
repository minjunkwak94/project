from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.shortcuts import render, get_object_or_404
from .models import Post, Comment
from .serializers import PostListSerializer, PostDetailSerializer, CommentListSerializer, CommentDetailSerializer


@api_view(['GET', 'POST'])
def post_list_create(request):
    if request.method == 'GET':
        posts = Post.objects.all()
        serializer = PostListSerializer(posts, many=True)
        return Response(serializer.data)
    else:
        serializer = PostDetailSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)


@api_view(['GET', 'PUT', 'DELETE'])
def post_detail_update_delete(request, post_pk):
    post = get_object_or_404(Post, pk=post_pk)
    if request.method == 'GET':
        serializer = PostDetailSerializer(post)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = PostDetailSerializer(post, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
    else:
        post.delete()
        return Response({ 'success delete post!': post_pk })


@api_view(['GET', 'POST'])
def comment_list_create(request, post_pk):
    post = get_object_or_404(Post, pk=post_pk)
    if request.method == 'GET':
        comments = post.comment_set.all()
        serializer = CommentListSerializer(comments, many=True)
        return Response(serializer.data)
    else:
        serializer = CommentListSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            comment = serializer.save(post=post)
            return Response(serializer.data)


@api_view(['DELETE'])
def comment_delete(request, post_pk, comment_pk):
    post = get_object_or_404(Post, pk=post_pk)
    comment = get_object_or_404(Comment, post=post, pk=comment_pk)
    comment.delete()
    return Response({ 'success delete comment!': comment_pk })