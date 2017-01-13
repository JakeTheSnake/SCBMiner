from django.shortcuts import render
from django.http import HttpResponse


def highscores(request):
  return HttpResponse("hi")
