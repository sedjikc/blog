from django.contrib import admin
from .models import Post, Comments

class PostInline(admin.StackedInline):
    model = Comments
    extra = 1

class PostAdmin(admin.ModelAdmin):
    fields = ['author', 'title', 'text', 'created_date', 'published_date']
    inlines = [PostInline]
    list_filter = ['published_date']

admin.site.register(Post, PostAdmin)