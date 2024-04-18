from django.contrib import admin
from .models import Book,Comment
class CommentAdmin(admin.ModelAdmin):
    list_display = ['text','user','datetime_created']
admin.site.register(Book)
admin.site.register(Comment,CommentAdmin)

