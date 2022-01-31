from django.shortcuts import render,redirect
from .models import Register
from django.core.mail import send_mail
from Blog_Project.settings import EMAIL_HOST_USER
from django.contrib.auth import (
    login,
    logout,
    authenticate,
)
# Create your views here.
def register(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        repeat_password = request.POST.get('repeat_password')
        if password == repeat_password:
            user = Register.objects.create_user(name=name, password=password, email=email,confirm_password=repeat_password)
            user.save()
            subject = 'Welcome to blog app'
            message = 'your name is '+ name  + ' ' + "your email is" + ' ' + email
            recepient = (email)
            send_mail(subject,message, EMAIL_HOST_USER, [recepient], fail_silently = False)
            return redirect("Account:login")
        else:
            return redirect("Account:register")
    return render(request,'account/register.html')

def userlogin(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(email=email, password=password ,name=name)
        if user:
            login(request, user)
            return redirect('PostApp:show')
        else:
            return redirect("Account:login")
    return render(request,'account/login.html')

def userlogout(request):
    logout(request)
    return redirect('Account:login')