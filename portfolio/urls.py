"""portfolio URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from blog import views

# static files
#from django.contrib.staticfiles import static
from django.conf.urls.static import static
from portfolio import settings
from blog.feeds import LatestPostsFeed
from blog.models import Post
#from django.conf.urls import include


# contrib imports
from django_distill import distill_path

# distill functions
def get_index():
    return None

def get_blog_posts():
    for post in Post.objects.all():
        yield {'slug': post.slug}


urlpatterns = [
    # builtin modules
    path('admin/', admin.site.urls),
    path('martor/', include('martor.urls')),
    # custom views
    distill_path('', views.PostList.as_view(), name='home', distill_func=get_index, distill_file='index.html'),
    distill_path('post/<slug:slug>/', views.PostDetail.as_view(), name='post_detail', distill_func=get_blog_posts),
    distill_path('feed/rss', LatestPostsFeed(), name='post_feed', distill_func=get_index),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
