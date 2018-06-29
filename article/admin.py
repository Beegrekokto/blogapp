from django.contrib import admin
from .models import Article, Like, Comment

# Register your models here.

admin.site.register(Article)
admin.site.register(Like)
admin.site.register(Comment)