from django.shortcuts import render
from Mapp.models import movie
from Mapp import views
from Mapp.forms import movieform
from django.views.generic import ListView,DetailView,CreateView,DeleteView,UpdateView
from django.urls import reverse_lazy
# Create your views here.
# def home(request):
#     l=movie.objects.all()
#     return render(request,'home.html',{'l':l})
class home(ListView):
    model=movie
    template_name="home.html"
    context_object_name="l"
# def addmovie(request):
#     if (request.method=="POST"):
#         t=request.POST['t']
#         d=request.POST['d']
#         s=request.POST['s']
#         l=movie.objects.create(title=t,desc=d,img=s)
#         l.save()
#         return home(request)
#     return render(request,'addmovies.html')
# def update(request,p):
#     b=movie.objects.get(id=p)
#     f=movieform(instance=b)
#     if(request.method=="POST"):
#         f=movieform(request.POST,request.FILES,instance=b)
#         if(f.is_valid()):
#             f.save()
#             return home(request)
#     return render(request,'addmovies.html',{'f':f})
"""def add1(request):
    f = movieform()
    if (request.method == "POST"):
        f = movieform(request.POST, request.FILES)
        if (f.is_valid()):
            f.save()
            return home(request)
    return render(request, 'addmovies.html', {'f': f})"""
class add1(CreateView):
    model= movie
    template_name="addmovies.html"
    fields = ['title','desc','img']
    success_url = reverse_lazy('Mapp:home')
# def view(request,p):
#     v=movie.objects.get(id=p)
#     return render(request,'view.html',{'view':v})
class view(DetailView):
    model = movie
    template_name = "view.html"
    context_object_name = "view"
# def delete(request,p):
#     d=movie.objects.get(id=p)
#     d.delete()
#     return home(request)
class delete(DeleteView):
    model=movie
    template_name="delete.html"
    success_url=reverse_lazy('Mapp:home')

class update(UpdateView):
    model = movie
    template_name = "addmovies.html"
    fields = ['title', 'desc', 'img']
    success_url = reverse_lazy('Mapp:home')