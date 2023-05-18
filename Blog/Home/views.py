from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core.mail import EmailMessage
from .forms import RegistrationForm
from Blog.models import MyPost
from Blog.models import MyPostForm

# Create your views here.
def index(request):
    return render(request,'pages/home.html')
def info(request):
    return render(request,'pages/info.html')
def blog(request):
    myposts = MyPost.objects.all()
    return render(request,'pages/blog.html',{'myposts':myposts})
def search(request):
    query = request.POST.get('query')
    if query is None:
        myposts = MyPost.objects.all()
    else:
        myposts = MyPost.objects.filter(title__icontains=query) | MyPost.objects.filter(content__icontains=query)
    return render(request, 'pages/blog.html', {'myposts': myposts, 'query': query})



def create_mypost(request):
    if request.method == 'POST':
        form = MyPostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/blog') 
    else:
        form = MyPostForm()
    return render(request, 'pages/create_mypost.html', {'form': form})


def contact(request):
    if request.method == 'POST':
        first_name = request.POST.get('firstName', '')
        last_name = request.POST.get('lastName', '')
        email = request.POST.get('email', '')
        message = request.POST.get('message', '')
       
        # Gửi email đến địa chỉ mặc định
        email = EmailMessage(
            subject='Contact Form Submission',
            body=f'From: {first_name} {last_name} <{email}>\n\n{message}',
           
        )
        email.to = ['wiki212002@gmail.com']
        email.send()

        # Trả về trang "Gửi email thành công"
        return render(request, 'pages/home.html')

    # Nếu method là GET, hiển thị form để điền thông tin
    return render(request, 'pages/contact.html')
def register(request):
    form = RegistrationForm()
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'pages/home.html')
    return render(request, 'pages/register.html', {'form': form})
