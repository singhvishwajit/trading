from django.contrib import admin
from tinymce.widgets import TinyMCE
from .models import Post
from django.db import models


class PostAdmin(admin.ModelAdmin):
	fieldsets = [
        ("Title/date", {'fields': ["title", "date_posted"]}),
        ("Content", {"fields": ["content"]}),
        ("Details", {"fields": ["details"]}),
        ("Slug", {"fields": ["slug"]}),
        ("Author", {"fields": ["author"]}),
        ("Thumbnail", {"fields": ["thumbnail"]})
    ]

	formfield_overrides = {
	models.TextField: {'widget': TinyMCE()}
	}



admin.site.register(Post, PostAdmin)