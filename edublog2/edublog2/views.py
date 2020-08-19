from django.shortcuts import render
from posts.models import Post
from django.core.paginator import Paginator

def index(request):
    if request.user.is_authenticated:
        posts=Post.objects.all()
        paginator = Paginator(posts, 10) # Show 25 contacts per page.

        page_number = request.GET.get('page')
        posts= paginator.get_page(page_number)
        page_obj= paginator.get_page(page_number)
        return render(request,'../templates/index.html',{'posts':posts,'page_obj': page_obj})
    return render(request, '../templates/home.html')
  

      
