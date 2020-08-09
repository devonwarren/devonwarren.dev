from django.contrib import admin

from .models import Post 
from portfolio.settings import STATIC_URL

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_on', 'updated_on']
    search_fields = ['title', 'content']
    
    class Media:
        css = {
        'all': (STATIC_URL + 'css/monokai.css',)
        }
