from django.urls import path
from . import views
app_name = 'Account'

urlpatterns = [
    path('register/',views.register,name="register"),
    path('login/',views.userlogin,name="login"),
    path('user_logout/',views.userlogout,name="logout"),
]