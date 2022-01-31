from django.shortcuts import render,redirect,HttpResponseRedirect
from . import models
from django.core.paginator import Paginator
# Create your views here.



def ShowPost(request):
    All_Post = models.Post.objects.all()
    paginator = Paginator(All_Post,4)
    page = request.GET.get('page')
    paged_post = paginator.get_page(page)
    return render(request,"Post/blog.html",{"All_Post":paged_post})

def UserPost(request):
    user_Post = models.Post.objects.filter(author=request.user.id)
    paginator = Paginator(user_Post,4)
    page = request.GET.get('page')
    paged_post = paginator.get_page(page)
    return render(request,"Post/user_post.html",{"All_Post":paged_post})


def CreatePost(request):
    if request.method == "POST":
        author = models.Register.objects.get(id=request.user.id)
        title = request.POST.get("title")
        body = request.POST.get("body")
        image = request.FILES.get('image')
        PostCreate = models.Post.objects.create(title=title,body=body,author=author,image=image)
        return redirect("PostApp:show")
    return render(request,"Post/create.html")

def PostDetail(request,id):
    DetailPost = models.Post.objects.get(id=id)
    RelatedPost = models.Post.objects.all().order_by('-created')[:4]
    comment = models.Comment.objects.all()
    fav = bool
    if DetailPost.favourties.filter(id=request.user.id).exists():
        fav = True
    if request.method == "POST":
        user = models.Register.objects.get(id=request.user.id)
        name = request.POST.get("name")
        message = request.POST.get("message")
        com = models.Comment.objects.create(name=name,message=message,post=DetailPost,author=user)
        return redirect("PostApp:show")
    return render(request,"Post/detail.html",{"postdetail":DetailPost,"relatedpost":RelatedPost,"comments":comment,'fav':fav})

def UpdatePost(request,id):
    blog = models.Post.objects.get(id=id)
    if request.method == "POST":
        name = request.POST.get("title")
        work = request.POST.get("body")
        image = request.FILES.get('image')
        blog.title = name
        blog.body = work
        blog.image = image
        blog.save()
        return redirect("PostApp:show")
    return render(request,"Post/update.html",{"blog":blog})

def DeletePost(request,id):
    blog = models.Post.objects.get(id=id)
    if request.method == "POST":
        blog.delete()
        return redirect("PostApp:show")
    return render(request,"Post/delete.html")


def add_fav(request,id):
    fav = models.Post.objects.get(id=id)
    if fav.favourties.filter(id=request.user.id).exists():
        fav.favourties.remove(request.user)
    else:
        fav.favourties.add(request.user)
    return HttpResponseRedirect(request.META['HTTP_REFERER'])
    
def ShowLike(request):
    blog = models.Register.objects.get(id=request.user.id)
    com = models.Comment.objects.all()
    new = models.Post.objects.filter(favourties=request.user)
    return render(request,"Post/showprofile.html",{'com':com,'blog':blog,'new':new})