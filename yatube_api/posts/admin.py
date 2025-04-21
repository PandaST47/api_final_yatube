# Удаляем неиспользуемый импорт или регистрируем модели в админке
from django.contrib import admin
from .models import Post, Comment, Follow, Group

admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Follow)
admin.site.register(Group)
