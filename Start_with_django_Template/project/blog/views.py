from django.shortcuts import render,get_object_or_404,redirect
from .models import Blog
from .froms import BlogForm
from django.views.generic import ListView,UpdateView,DeleteView,CreateView
#============================= FUNCTION BASED VIEW =========================#
def list_blog(request):
    context={
        'blog':Blog.objects.all()
    }
    return render(request,'pages/index.html',context)

def detail_blog(request,pk):
    context={
        'blog':get_object_or_404(Blog,pk=pk)
    }
    return render(request,'pages/detail_blog.html',context)

def add_blog(request):
    if request.method=='POST':
        form=BlogForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('list_blog')
    else:
        form=BlogForm()
    context={
        "form":form
    }
    return render(request,'pages/create_blog.html',context)
        
def update_blog(request,pk):
    blog_id=Blog.objects.get(pk=pk)
    if request.method=='POST':
        form=BlogForm(request.POST,request.FILES,instance=blog_id)
        if form.is_valid():
            form.save()
            return redirect('list_blog',pk=blog_id)
    else:
        form=BlogForm(instance=blog_id)
    return render(request,'pages/update_blog.html',{"form":form})

def delete_blog(request,pk):
    blog=Blog.objects.get(pk=pk)
    if request.method=='POST':
       blog.delete()
       return redirect('list_blog')
    return render(request,'pages/delete_blog.html',{'blog':blog})

#=============================  Class BASED VIEW =========================#
class ListViewBlog(ListView):
    model=Blog
    template_name='pages/index.html'
    context_object_name='blog'

class DetailViewBlog(DeleteView):
   model=Blog
   template_name='pages/detail_blog.html'
   context_object_name='blog'

class UpdateViewBlog(UpdateView):
    model=Blog
    form_class=BlogForm
    context_object_name='form'
    success_url='/'
    template_name='pages/update_blog.html'

class CreateViewBlog(CreateView):
    model=Blog
    form_class=BlogForm
    context_object_name='form'
    success_url='/'
    template_name='pages/update_blog.html'


class DeleteViewBlog(DeleteView):
    model=Blog
    template_name='pages/delete_blog.html'
    success_url='/'
    context_object_name='blog'