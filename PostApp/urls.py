from django.urls import path
from . import views
app_name = 'PostApp'

urlpatterns = [
    path("show/",views.ShowPost,name="show"),
    path("UserPost/",views.UserPost,name="UserPost"),
    path("detail/<id>",views.PostDetail,name='PostDetail'),
    path("CreatePost/",views.CreatePost,name="CreatePost"),
    path("update/<id>",views.UpdatePost,name="UpdatePost"),
    path("delete/<id>",views.DeletePost,name="DeletePost"),
    path("add_fav/<id>",views.add_fav,name="add_fav"),
    path("ShowLike",views.ShowLike,name="ShowLike"),

]