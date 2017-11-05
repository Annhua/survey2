from django.shortcuts import render,HttpResponse,redirect

# Create your views here.
from APP01 import models
from django.http import JsonResponse
import copy
from django.http import QueryDict

import json
def index(request):
    if request.method=='POST':
        parmes=copy.deepcopy(request.POST)
        parmes._mutable=True
        del parmes['csrfmiddlewaretoken']
        del parmes['title']
        dic={}
        print(parmes)
        for item in parmes:
            print('=========',parmes.getlist(item))
            name,num=item.split('-')
            print(name)
            if num not in dic:
                dic.setdefault(num,{})
                temp={name:parmes.getlist(item)}
                # print(name)

                print(temp)
                # print('-----',temp)
                dic[num].update(temp)
        print('+++++',dic)




    return render(request,'index.html')


def add(request):
    if request.method=='GET':
        sur=models.SurveryItem.answer_type_choices
        survery=models.Survery.objects.all()

        response = {

                'status_choices': sur,


            }


        return JsonResponse(response)

    else:
        print(request.POST)

