from django import http

from django.shortcuts import render


def view(request):
    return http.HttpResponse("It Works")

