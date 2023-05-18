from django.db import models
from django import forms


# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField()
    date = models.DateTimeField(auto_now_add= True)
    def __str__(self):
        return self.title

class Course(models.Model):
    name = models.CharField(max_length=100)
    content = models.TextField()
    price = models.IntegerField()
    person = models.TextField()
    date = models.DateTimeField(auto_now_add= True)
    def __str__(self):
        return self.name

class MyPost(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    image = models.ImageField(null= True)
    writtenby = models.CharField(max_length=100)
    date = models.DateTimeField(auto_now_add= True)
    audio_file = models.FileField(upload_to='media/music', null=True)
    def __str__(self):
        return self.title

class MyPostForm(forms.ModelForm):
    class Meta:
        model = MyPost
        fields = ('title', 'content', 'image', 'writtenby', 'audio_file')