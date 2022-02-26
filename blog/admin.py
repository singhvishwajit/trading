from django.contrib import admin
from tinymce.widgets import TinyMCE
from .models import Investing, Research, Protocol
from django.db import models


class InvestingAdmin(admin.ModelAdmin):
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


class ResearchAdmin(admin.ModelAdmin):
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


class ProtocolAdmin(admin.ModelAdmin):
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

admin.site.register(Investing, InvestingAdmin)
admin.site.register(Research, ResearchAdmin)
admin.site.register(Protocol, ProtocolAdmin)