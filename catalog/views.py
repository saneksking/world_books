from django.shortcuts import render, HttpResponse


def index(request):
    return HttpResponse("Home site's page World of books")
