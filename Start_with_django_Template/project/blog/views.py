from django.shortcuts import render
from .models import Blog
def index(request):
    context={
        'context':Blog.objects.all()
    }
    return render(request,'pages/index.html',context)
