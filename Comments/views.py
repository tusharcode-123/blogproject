from django.shortcuts import render,redirect
from PostApp.models import Comment
# Create your views here.

def CommentUpdate(request,id):
    comment_id = Comment.objects.get(id=id)
    if request.method == "POST":
        message = request.POST.get("message")
        comment_id.message = message
        comment_id.save()
        return redirect("PostApp:show")

    return render(request,"Comment/commentupdate.html",{"comment":comment_id})

def CommentDelete(request,id):
    blog = Comment.objects.get(id=id)
    if request.method == "POST":
        blog.delete()
        return redirect("PostApp:show")
    return render(request,"Comment/commentdelete.html")