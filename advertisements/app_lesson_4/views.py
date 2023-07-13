from django.shortcuts import render
from django.http import HttpResponse

def index_(request):
    return HttpResponse('Домашка по 4 занятию')
# Create your views here.
