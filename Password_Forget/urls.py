from django.urls import path
from . import views
app_name = 'Password'

urlpatterns = [
    path("password_reset/",views.password_reset,name="password_reset"),
    path("password_reset/done/",views.password_reset_done,name="password_reset_done"),
    path("reset/<uidb64>/<token>/", views.password_reset_confirm, name='password_reset_confirm'),
    path("reset/done/",views.Password_reset_complete,name="Password_reset_complete"),
]