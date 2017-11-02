from django.shortcuts import render,HttpResponse,redirect

# Create your views here.
from APP01 import models
from django.http import JsonResponse

import json
def index(request):

    print(request.POST)
    return render(request,'index.html')


def add(request):
    if request.method=='GET':
        sur=models.SurveryItem.answer_type_choices

        response = {

                'status_choices': sur
            }


        return JsonResponse(response)

    else:
        print(request.POST)

