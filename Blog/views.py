from django.shortcuts import render
from .models import MyPost
# Create your views here.
def detailpost(request,id):
    myposts = MyPost.objects.get(id=id)
    return render(request,'blog.html',{'myposts':myposts})
