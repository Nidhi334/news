from django.shortcuts import render
from .models import  Category, Post
from django.db.models import Q

# Create your views here.

def index(request , category=None):
    data = {} 
    data['categories'] = Category.objects.all()
    data['posts'] = Post.objects.all()


    if(category is not None):
        data['posts'] = Post.objects.filter(category__cat_title=category)
    return render(request, 'index.html',data)

def viewpost(request,postid):
   postid = Post.objects.get(id=postid)
   return render(request, "view.html",{'post':postid})

def search (request):
    data = {}
    data['categories'] = Category.objects.all()
    search = request.GET.get('search')
    query = Q(title__icontains=search) | Q(author__icontains=search)
    data['posts'] = Post.objects.filter(query)
    return render(request, "index.html",data)


