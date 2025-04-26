from django.contrib import admin
from .models import Post, Comment
from django_summernote.admin import SummernoteModelAdmin 
# The ready-made SummernoteModelAdmin class defines the text editor
# enabling you to access its functionality in the admin panel for your posts.

@admin.register(Post)
# The @admin.register decorator is a shortcut to register the model with the admin site.
class PostAdmin(SummernoteModelAdmin):
    list_display = ("title", "slug", "status")
    search_fields = ["title"]
    list_filter = ("status",)
    prepopulated_fields = {"slug": ("title",)}
    summernote_fields = ("content",)

# Register your models here.
# admin.site.register(Post) - now redundant by the decorator
admin.site.register(Comment)