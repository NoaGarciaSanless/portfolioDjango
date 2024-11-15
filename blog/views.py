from django.shortcuts import render
from .models import Blogs

# Create your views here.

def all_blogs(request):
    # Selects all the blogs, and returns them in descending order
    all_blogs = Blogs.objects.all().order_by('-date')
    return render(request, 'blog/all_blogs.html', {"blogs": all_blogs})