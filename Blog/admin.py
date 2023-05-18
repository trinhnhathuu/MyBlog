from django.contrib import admin

from .models import MyPost, Post,Course


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'date')
    list_filter = ("date",)
    search_fields = ['title','body']
admin.site.register(Post, PostAdmin)

class CourseAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'person')
    list_filter = ("price",)
    search_fields = ['name','content']
    
admin.site.register(Course, CourseAdmin)

class MyPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'writtenby')
    list_filter = ("writtenby",)
    search_fields = ['title','content']

admin.site.register(MyPost, MyPostAdmin)