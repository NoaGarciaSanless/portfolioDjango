from django.shortcuts import render, get_object_or_404
from .models import Blogs

# Create your views here.

def all_blogs(request):
    # Selects all the blogs, and returns them in descending order
    all_blogs = Blogs.objects.all().order_by('-date')
    return render(request, 'blog/all_blogs.html', {"blogs": all_blogs})

def details(request, blog_id):
    blog = get_object_or_404(Blogs, pk=blog_id)
    return render(request, 'blog/details.html', {'blog' : blog})