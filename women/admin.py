from django.contrib import admin
from .models import *


class WomenAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'time_create', 'photo', 'is_published')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'content')
    list_editable = ('is_published',)
    list_filter = ('is_published', 'time_create')
    prepopulated_fields = {"slug":("title",)}


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'slug')
    list_display_links = ('id', 'name')
    search_fields = ('name',)
    prepopulated_fields = {"slug": ("name",)}


class MenuAdmin(admin.ModelAdmin):
    list_display = ('title', 'url_name')
    list_display_links = ('title',)


admin.site.register(Women, WomenAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Menu, MenuAdmin)
