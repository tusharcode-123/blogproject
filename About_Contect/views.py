from django.shortcuts import render
from .models import About,Contect
from PostApp.models import Post
from django.core.mail import send_mail
from Blog_Project.settings import EMAIL_HOST_USER
# Create your views here.

def Home(request):
    LetestPost = Post.objects.all().order_by('-created')[:4]
    return render(request,"Post/home.html",{"LetestPost":LetestPost})

def about(request):
    about_as = About.objects.all()
    return render(request,"About_Contect/about.html",{"about_as":about_as})


def contect(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        message = request.POST.get("message")
        Contect.objects.create(Name=name,Email=email,Phone=phone,Message=message)
        subject = 'Welcome to blog app'
        message = 'your name is '+ name  + ' ' + "your email is" + ' ' + email + ' ' + "your message is" + ' ' + message 
        recepient = (email)
        send_mail(subject,message, EMAIL_HOST_USER, [recepient], fail_silently = False)
    return render(request,"About_Contect/contect.html")