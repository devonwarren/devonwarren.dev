from django.contrib.syndication.views import Feed
from django.template.defaultfilters import truncatewords
from .models import Post
from django.urls import reverse


class LatestPostsFeed(Feed):
    title = "Devon Warren blog posts"
    link = ""
    description = "New posts on my devonwarren.dev blog"

    def items(self):
        return Post.objects.all()

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return truncatewords(item.content, 30)