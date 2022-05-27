from django.contrib import admin

# Register your models here.
from .models import Feedback, Category


@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    fields = ['title', 'content', 'is_published', 'slug','cat']
    list_display = ('id', 'title', 'time_create', 'is_published','cat')
    list_display_links = ('title',)
    search_fields = ('title', 'content')
    list_editable = ('is_published',)
    list_filter = ('is_published', 'time_create')
    prepopulated_fields = {'slug': ('title',)}


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('name',)
    search_fields = ('name',)
    prepopulated_fields = {'slug': ('name',)}
