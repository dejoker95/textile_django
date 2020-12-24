from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .forms import ImageForm
from .models import Image, CrawledData
from django.db import connection
# Create your views here.


def index(request):
    if request.method == "GET":
        form = ImageForm()
        #data = CrawledData.objects.filter(id='110100000001')
        data = CrawledData.objects.raw(
            'select id,img From crawled_data LIMIT 3')
        print(data[2].img)
    elif request.method == "POST":
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/result')

    context = {
        'form': form,
        'data': data
    }
    return render(request, 'frontpage/index.html', context)


def show_list(request):
    images = Image.objects.all()
    print(images)
    context = {'images': images}
    return render(request, 'frontpage/list.html', context)


def result(request):
    images = Image.objects.last()
# test
    data = CrawledData.objects.raw(
        'select id,img From crawled_data LIMIT 10')
    print(data[0].img)
    # context = {
    #     'data': data,
    #     'row1': data[0]}

    context = {
        'images': images,
        'row1': data[0],
        'row2': data[1],
        'row3': data[2],
        'row4': data[3],
        'row5': data[4],
        'row6': data[5],
        'row7': data[6],
        'row8': data[7],
        'row9': data[8],
        'row10': data[9]}

    return render(request, 'frontpage/result.html', context)


# def clothes(request):
#     data = CrawledData.objects.raw(
#         'select id,img From crawled_data LIMIT 3')
#     print(data[0].img)
#     context = {
#         'data': data,
#         'row1': data[0]}

#     return render(request, 'frontpage/grid.html', context)
