from django.shortcuts import render
from django.http import HttpResponse


def welcome(request):
    return HttpResponse("Hello Lemon")
