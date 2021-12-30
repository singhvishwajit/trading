from django.contrib import admin
from tinymce.widgets import TinyMCE
from .models import Trading, DeFi, Project, Investment
from django.db import models


class TradingAdmin(admin.ModelAdmin):
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


class DeFiAdmin(admin.ModelAdmin):
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


class ProjectAdmin(admin.ModelAdmin):
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

class InvestmentAdmin(admin.ModelAdmin):
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


admin.site.register(Trading, TradingAdmin)
admin.site.register(DeFi, DeFiAdmin)
admin.site.register(Project, ProjectAdmin)
admin.site.register(Investment, InvestmentAdmin)