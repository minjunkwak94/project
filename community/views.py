from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods, require_POST
from .models import Post, Comment
from .forms import PostForm, CommentForm

from django.core.paginator import Paginator


# Create your views here.
def index(request):
    posts = Post.objects.order_by('-pk')
    paginator = Paginator(posts, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        # 'posts': posts,
        'page_obj':page_obj,
    }
    return render(request, 'community/index.html', context)


@login_required
@require_http_methods(['GET', 'POST'])
def create(request):
    if request.method == 'POST':
        form = PostForm(request.POST) 
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            return redirect('community:detail', post.pk)
    else:
        form = PostForm()
    context = {
        'form': form,
    }
    return render(request, 'community/create.html', context)


def detail(request, post_pk):    
    post = get_object_or_404(Post, pk=post_pk)
    form = PostForm(instance=post)
    comment_form = CommentForm()
    comments = post.comment_set.all()
    context = {
        'post': post,
        'form' : form,
        'comment_form': comment_form,
        'comments': comments,
    }
    return render(request, 'community/detail.html', context)


@login_required
@require_http_methods(['GET', 'POST'])
def update(request, post_pk):
    # Post = Post.objects.get(pk=pk)
    Post = get_object_or_404(Post, pk=post_pk)
    # 수정하는 유저와, 게시글 작성 유저가 같은지 ?
    if request.user == Post.user:
        if request.method == 'POST':
            form = PostForm(request.POST, instance=Post)
            if form.is_valid():
                form.save()
                return redirect('community:detail', Post.pk)
        else:
            form = PostForm(instance=Post)
    else:
        return redirect('community:index')
    context = {
        'form': form,
        'Post': Post,
    }
    return render(request, 'community/update.html', context)


@require_POST
def delete(request, post_pk):
    if request.user.is_authenticated:
        # Post = Post.objects.get(pk=pk)
        post = get_object_or_404(Post, pk=post_pk)
        if request.user == Post.user:
            post.delete()
            return redirect('community:index')
    return redirect('community:detail', Post.pk)


@require_POST
def comments_create(request, post_pk):    
    if request.user.is_authenticated:
        post = get_object_or_404(Post, pk=post_pk)
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            # Create, but don't save the new comment instance.
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.user = request.user
            comment.save()
            return redirect('community:detail', post.pk)
        context = {
            'comment_form': comment_form,
            'post': post,
        }
        return render(request, 'community/detail.html', context)
    return redirect('accounts:login')


@require_POST
def comments_delete(request, post_pk, comment_pk):
    # comment = Comment.objects.get(pk=comment_pk)
    if request.user.is_authenticated:
        comment = get_object_or_404(Comment, pk=comment_pk)
        if request.user == comment.user:
            comment.delete()
    return redirect('community:detail', post_pk)

def pur_posts(request, category_pk):
    if int(category_pk) > 3:
        return redirect('community:posts')
    posts = Post.objects.filter(category=category_pk).order_by('-id')
    paginator = Paginator(posts, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'posts': posts,
        'page_obj': page_obj,
        'category_pk': category_pk,
    }
    return render(request, 'community/index.html', context)

