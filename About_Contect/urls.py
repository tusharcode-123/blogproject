from django.urls import path
from . import views
app_name = 'About_Contect'

urlpatterns = [
    path("",views.Home,name="Home"),
    path("About/",views.about,name="About"),
    path("Contect/",views.contect,name="contect"),
]