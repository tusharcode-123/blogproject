from django.shortcuts import redirect, render
from account.models import Register
from django.db.models.query_utils import Q
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes,force_text
from django.contrib.sites.shortcuts import get_current_site
from Blog_Project.settings import EMAIL_HOST_USER
from django.http import HttpResponse
from django.core.mail import  send_mail
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.contrib.auth.tokens import default_token_generator
# Create your views here.

def password_reset(request):
    if request.method == "POST":
        email = request.POST.get("email")
        print(email)
        user_email = Register.objects.filter(Q(email=email))
        print(user_email)
        if user_email.exists():
            for user in user_email:
                current_site = get_current_site(request)
                subject = 'Activate your Account'
                email_template_name = "password/password_reset_email.txt"
                message =  {
                    'user': user.email,
                    'domain': current_site.domain,
                    'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                    'token': default_token_generator.make_token(user),
                    'protocol': 'https',
                }
                email = render_to_string(email_template_name,message)
                try:
                    send_mail(subject,email,'EMAIL_HOST_USER',[user.email],fail_silently=False)
                except:
                    return HttpResponse('invalid')
                
                return redirect("Password:password_reset_done")
        else:
            return redirect("Password:password_reset")
    return render(request,"password/password_reset.html")

def password_reset_done(request):
    return render(request,"password/password_reset_done.html")

def password_reset_confirm(request,uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = Register.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, user.DoesNotExist):
        user = None
    if user is not None and default_token_generator.check_token(user, token):
        if request.method == "POST":
            new_password1 = request.POST.get("new_password1")
            new_password2 = request.POST.get("new_password2")
            if new_password1 == new_password2:
                user.set_password(new_password1)
                user.confirm_password = new_password2
                user.save()
                return redirect("Password:Password_reset_complete")
            else:
                return redirect("Password:password_reset_confirm")
    return render(request,"password/password_reset_confirm.html")

def Password_reset_complete(request):
    return render(request,"password/password_reset_complete.html")