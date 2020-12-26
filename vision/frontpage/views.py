from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .forms import ImageForm

from .models import Image, CrawledData
from django.db import connection

from .serializers import ImageSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response

import requests
import json
from urllib import parse
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
    serializers = ImageSerializer(images)
    image_url = serializers.data['image'].split('/')[-1]

    # 여기서 사진 주소만 넣었음. 앞에 localhost/media/~~ 이런거 넣으니깐 인식을 못함. ~~.png 만 존재. 나머지 앞 부분 ec2주소/media  는 모델팀 컴터에서 해야함.
    print(image_url)
# test
    url = 'http://13.125.191.170:8000/vector/{0}'.format(image_url)
    print(url)
    json_data = requests.get(url)
    data = json_data.json()
    print(data)
    query = 'select id, img from crawled_data where id={0} \
or id={1} or id={2} or id={3} or id={4} or id={5} or \
id={6} or id={7} or id={8} or id={9}'.format(data[0]['id'], data[1]['id'], data[2]['id'], data[3]['id'], data[4]['id'], data[5]['id'], data[6]['id'], data[7]['id'], data[8]['id'], data[9]['id'])

    # a = 10
    # query = 'select id,img From crawled_data LIMIT '+str(a)

    data = CrawledData.objects.raw(
        query)
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

@api_view(['GET'])
def image_list(request):
    images = Image.objects.last()
    serializers = ImageSerializer(images)
    return Response(serializers.data)


#     return render(request, 'frontpage/grid.html', context)
