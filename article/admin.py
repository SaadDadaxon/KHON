from django.contrib import admin
from .models import Article


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'is_deleted', 'modified_date', 'created_date']
    prepopulated_fields = {'slug': ('title', )}
#     readonly_fields = ['modified_date', 'created_date']
#     fields = ['title', 'image', 'content', 'modified_date', 'created_date']
#     list_display_links = ['id', 'title']
#     list_per_page = 10
#     ordering = ['-id']
#     search_fields = ['title']
#     search_help_text = "'title' orqali qidir"
#     list_filter = ['modified_date', 'created_date']
#     date_hierarchy = 'created_date'


# admin.site.register(Article)
