# coding: utf-8
# Register your models here.

from django.contrib import admin
from blog.models import Post, Comment

admin.site.register(Post)
admin.site.register(Comment)
