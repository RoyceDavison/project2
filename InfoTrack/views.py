from django.shortcuts import render

# Create your views here.
from .models import User, Comment, Post

def index(request):
   
    # Generate counts of some of the main objects
    num_users=User.objects.all().count()
    num_posts=Post.objects.all().count()
    num_comments=Comment.objects.all().count()
    
    # Render the HTML template index.html with the data in the context variable
    return render(
        request,
        'index.html',
        context={'num_users':num_users,
                 'num_posts':num_posts,
                 'num_commands':num_comments,        
        }
    )


def rides(request):
    # Render the HTML template index.html with the data in the context variable
    return render(
        request,
        'ride_temp.html',
        context={'post_titile':post_title,
                 'post_time':post_time,
                 'post_detail':post_detail,
                 'user':user,
                }
        )
