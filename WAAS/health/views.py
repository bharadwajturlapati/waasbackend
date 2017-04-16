from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def healthstatus(request) :
    return HttpResponse("hello");