from django.contrib import admin

from .models import Post 
from portfolio.settings import STATIC_URL

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_on', 'updated_on']
    search_fields = ['title', 'content']
    
    class Media:
        css = {
        'all': ('http://cdnjs.cloudflare.com/ajax/libs/highlight.js/10.1.2/styles/atom-one-dark.min.css',)
        }
