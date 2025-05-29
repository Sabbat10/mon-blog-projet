from django.contrib import admin

# models
from .models import Article

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'created_at', 'updated_at')
    search_fields = ('title', 'content', 'author__username')
    list_filter = ('author', 'created_at')


admin.site.register(Article, ArticleAdmin)
