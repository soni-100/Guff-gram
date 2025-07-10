from django.contrib import admin
from .models import Post
# Register your models here.

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('user', 'caption', 'created_at')
    list_filter = ('created_at', 'user')
    search_fields = ('caption', 'user__username')
    readonly_fields = ('created_at',)