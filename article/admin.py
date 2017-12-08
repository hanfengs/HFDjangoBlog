from django.contrib import admin
from article.models import *

# Register your models here.
class BookAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'pud_date', 'add_i', 'category')

admin.site.register(Book, BookAdmin)

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'content', 'book', 'date_time')

admin.site.register(Article, ArticleAdmin)
