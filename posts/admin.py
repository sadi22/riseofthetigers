from django.contrib import admin
from .models import Post, Category, Poll, Choice
from . import models


# Register your models here.


class PostModelAdmin(admin.ModelAdmin):
    list_display = ["title", "updated", "timestamp", "featured_post"]
    list_display_links = ["title"]

    list_filter = ["updated", "timestamp"]
    search_fields = ["title", "content"]



class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 2
    exclude = ["votes",]

class PollAdmin(admin.ModelAdmin):
    inlines = [
        ChoiceInline,
    ]

admin.site.register(Post, PostModelAdmin)
admin.site.register(Category)
admin.site.register(Poll, PollAdmin)

