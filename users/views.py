from django.http import HttpResponse
from django.shortcuts import render


def login(request):
    return HttpResponse("Логин")


def logout(request):
    return HttpResponse("logout")
