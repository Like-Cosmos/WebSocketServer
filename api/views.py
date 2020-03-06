from django.core.paginator import Paginator
from django.shortcuts import render

from api.models import JndUser
from django.http import JsonResponse, HttpResponseNotAllowed, HttpResponse
from rest_framework import status
import json
from .models import JndUser
from django.core import serializers
def selectinfo(request, *args, **kwargs):
    # 从models获取一个表数据
    temp = JndUser.objects.all()
    # 引入分页包，拆分每页十条
    Paginators = Paginator(temp,10)
    # 传入第几页
    print(Paginators.object_list)
    Paginators = Paginators.page(1)
    if request.method == 'GET':
        json_data = serializers.serialize('json', Paginators)
        json_data = json.loads(json_data)
        return JsonResponse(json_data, safe=False)


