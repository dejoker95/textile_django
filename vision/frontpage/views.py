from django.shortcuts import render, redirect
from django.http import HttpResponse,HttpResponseRedirect
from .forms import ImageForm
from .models import Image
# Create your views here.

def index(request):
    if request.method == "GET":
        form = ImageForm()
    elif request.method == "POST":
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/result')

    context = {
        'form': form
    }
    return render(request, 'frontpage/index.html',context)


def show_list(request):
    images = Image.objects.all()
    print(images)
    context = {'images':images}
    return render(request, 'frontpage/list.html', context)

def result(request):
    images= Image.objects.last()
    context={'images':images}
            
    return render(request,'frontpage/result.html',context)




