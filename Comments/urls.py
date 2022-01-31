from django.urls import path
from . import views
app_name = 'Comment'

urlpatterns = [
    path("CommentUpdate/<id>",views.CommentUpdate,name="CommentUpdate"),
    path("CommentDelete/<id>",views.CommentDelete,name="CommentDelete"),
]