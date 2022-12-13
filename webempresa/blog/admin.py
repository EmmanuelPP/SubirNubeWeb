from django.contrib import admin
from .models import Category, Post

# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')


class PostAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    list_display = ('tittle', 'author', 'published', 'post_categories')
    ordering = ('tittle',)
    search_fields = ('tittle', 'author__username', 'categories__name')
    date_hierarchy = 'published'
    list_filter = ('author__username', 'categories__name')

    def post_categories(self, obj):
        return ', '.join([ categoria.name for categoria in obj.categories.all().order_by('name')])
    post_categories.short_description = 'Categoria_Propia'


admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)