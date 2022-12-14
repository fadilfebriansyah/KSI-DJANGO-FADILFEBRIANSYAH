from django.http import HttpResponse
from django.shortcuts import render

def articles(request, year):
    year = year
    str = year
    return HttpResponse(year)


def about(request):
    return HttpResponse("ini about")

def index(request):
    context = {
        'heading':'Form Manual',
    }
    if request.method == 'POST':
        print("ini adalah method post")
        context['nickname'] = request.POST['nickname']
        context['alamat'] = request.POST['alamat']
    else:
        print("ini adalah method GET")
    return render(request, 'index.html', context)