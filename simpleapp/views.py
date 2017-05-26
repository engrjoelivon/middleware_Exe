from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.template.response import TemplateResponse, SimpleTemplateResponse


def test(request):
    #print("inside of view",request.path)
    return render(request,template_name="simpleapp/home.html",context={"name":"joel"})



def test2(request):

    50 / 0


    return  TemplateResponse(request,template="simpleapp/home.html",context={"name":"joel"})






