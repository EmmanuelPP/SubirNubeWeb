from django.shortcuts import get_list_or_404, render
from .models import Post, Category

# Create your views here.

def blog(request):
    posts = Post.objects.all()
    return render(request, 'blog/blog.html', {'posts':posts})


def category(request, category_id):
    category = get_list_or_404(Category, id = category_id )
    return render(request, "blog/category.html", {'category':category})

