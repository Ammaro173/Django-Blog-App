from django.contrib import admin
from .models import Article

# Register your models here.


# @admin.register(Article)
class AdminArticle(admin.ModelAdmin):
    list_display = ("title", "author", "date_created", "updated", "published")


admin.site.register(Article, AdminArticle)
