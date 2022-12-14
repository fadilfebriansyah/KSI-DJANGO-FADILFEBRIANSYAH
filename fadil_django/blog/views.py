from django.shortcuts import render
from .models import Post
from django.http import HttpResponse
# Create your views here.
def index(request):
    db = Post.objects.all()
    context = {
        'title':'Blog',
        'heading':'Blog',
        'subheading':'postingan',
        'post':db,
    }
    return render (request, 'blog/index.html',context)

def recent(request):
    return HttpResponse("ini blog")


def form(request):
    context = {
        'nama':'nama',
        'alamat':'alamat',
        'post':form,
    }
    if request.method == 'POST':
        print("ini adalah method post")
        context['nama'] = request.POST['nama']
        context['alamat'] = request.POST['alamat']
    else:
        print("ini adalah method get")
    return render (request, 'blog/form.html',context)