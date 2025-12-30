from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator
from .models import Post, Category, Comment
from .forms import CommentForm

def post_list(request, category_slug=None):
    posts = Post.objects.filter(status='published')
    
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        posts = posts.filter(category=category)
    
    # Pagination (6 posts per page)
    paginator = Paginator(posts, 6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    categories = Category.objects.all()
    
    context = {
        'page_obj': page_obj,
        'categories': categories,
        'category': category if category_slug else None,
    }
    return render(request, 'blog/list.html', context)

def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug, status='published')
    
    # Increment view count
    post.view_count += 1
    post.save(update_fields=['view_count'])
    
    # Handle comments
    comments = post.comments.filter(is_approved=True)
    new_comment = None
    
    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.post = post
            new_comment.save()
            return redirect('post_detail', slug=post.slug)
    else:
        comment_form = CommentForm()
    
    # Get related posts (same category)
    related_posts = Post.objects.filter(
        category=post.category, 
        status='published'
    ).exclude(id=post.id)[:3]
    
    context = {
        'post': post,
        'comments': comments,
        'new_comment': new_comment,
        'comment_form': comment_form,
        'related_posts': related_posts,
    }
    return render(request, 'blog/detail.html', context)

def post_list_by_tag(request, tag):
    posts = Post.objects.filter(
        status='published',
        tags__icontains=tag
    )
    context = {
        'posts': posts,
        'tag': tag,
    }
    return render(request, 'blog/post_list_by_tag.html', context)

def add_comment(request, slug):
    post = get_object_or_404(Post, slug=slug)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
    return redirect('post_detail', slug=slug)