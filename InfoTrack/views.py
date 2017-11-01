from django.shortcuts import render,redirect

# Create your views here.
from .models import User, Comment, Post

def homepage(request):
   
    # Generate counts of some of the main objects
    num_users=User.objects.all().count()
    num_posts=Post.objects.all().count()
    num_comments=Comment.objects.all().count()
    #num_videos = 
    # Render the HTML template index.html with the data in the context variable
    return render(
        request,
        #'index.html',
        "homepage.html",
        context={'num_users':num_users,
                 'num_posts':num_posts,
                 'num_comments':num_comments,        
        }
    )
def clubinfo(request):
    try:
        post = Post.objects.order_by("time")[0]
    except Post.DoesNotExist:
        raise Http404("Post does not exist")

    post_title = post.title
    post_time = post.time
    post_context = post.context
    return render(
        request,
        'clubinfo.html',
        context={'post_title':post_title,
                 'post_time':post_time,
                 'post_context':post_context,
                 #'user':user,
                }
        )

def freeride(request):
    # Render the HTML template index.html with the data in the context variable
    try:
        post = Post.objects.order_by("time")[0]
    except Post.DoesNotExist:
        raise Http404("Post does not exist")

    post_title = post.title
    post_time = post.time
    post_context = post.context
    return render(
        request,
        'freeride.html',
        context={'post_title':post_title,
                 'post_time':post_time,
                 'post_context':post_context,
                 #'user':user,
                }
        )

def courseinfo(request):
    # Render the HTML template index.html with the data in the context variable
    try:
        post = Post.objects.order_by("time")[0]
    except Post.DoesNotExist:
        raise Http404("Post does not exist")

    post_title = post.title
    post_time = post.time
    post_context = post.context
    return render(
        request,
        'courseinfo.html',
        context={'post_title':post_title,
                 'post_time':post_time,
                 'post_context':post_context,
                 #'user':user,
                }
        )
def freeride(request):
    # Render the HTML template index.html with the data in the context variable
    try:
        post = Post.objects.order_by("time")[0]
    except Post.DoesNotExist:
        raise Http404("Post does not exist")

    post_title = post.title
    post_time = post.time
    post_context = post.context
    return render(
        request,
        'freeride.html',
        context={'post_title':post_title,
                 'post_time':post_time,
                 'post_context':post_context,
                 #'user':user,
                }
        )
def privatetutor(request):
    # Render the HTML template index.html with the data in the context variable
    try:
        post = Post.objects.order_by("time")[0]
    except Post.DoesNotExist:
        raise Http404("Post does not exist")

    post_title = post.title
    post_time = post.time
    post_context = post.context
    return render(
        request,
        'privatetutor.html',
        context={'post_title':post_title,
                 'post_time':post_time,
                 'post_context':post_context,
                 #'user':user,
                }
        )

def rentinfo(request):
    # Render the HTML template index.html with the data in the context variable
    try:
        post = Post.objects.order_by("time")[0]
    except Post.DoesNotExist:
        raise Http404("Post does not exist")

    post_title = post.title
    post_time = post.time
    post_context = post.context
    return render(
        request,
        'rentinfo.html',
        context={'post_title':post_title,
                 'post_time':post_time,
                 'post_context':post_context,
                 #'user':user,
                }
        )