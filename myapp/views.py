from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

def home(request):
    return HttpResponse("<h1>Hello, World!</h1><p>This is the home page of my Django application.</p>")

def about(request):
    return HttpResponse("<h1>About</h1><p>This is the about page of my Django application.</p>")

#return an API endpoint response for the home page
def api_home(request):
    data = {
        "message": "Hello, World!",
        "description": "This is the home page of my Django application.",
        "version": "1.0.1",
        "date": "2026-10-28"
    }
    return JsonResponse(data)

#return an API endpoint response for the about page
def api_about(request):
    data = {
        "message": "About",
        "description": "This is the about page of my Django application.",
        "writer": "Muhammad Faseeh"
    }
    return JsonResponse(data)

