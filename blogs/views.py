from django.shortcuts import render, get_object_or_404
from .models import Blog


def blogs(request):
    """ Render all blogs """
    blogs = Blog.objects.all().order_by('-created_on')
    context = {
        'blogs': blogs,
    }

    return render(request, 'blogs/blogs.html', context)


def blog(request, blog_id):
    """ A view to show an individual blog """

    blog = get_object_or_404(Blog, pk=blog_id)

    context = {
        'blog': blog,
    }

    return render(request, 'blogs/blog.html', context)
