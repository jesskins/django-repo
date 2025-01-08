from django.shortcuts import render

# Create your views here.

def about_me(request):
    return HttpResponse("This would be the about page")

def index(request):
    if request.method == "GET":
        return HttpResponse("This was a GET request")
    elif request.method == "POST":
        return HttpResponse("You must have POSTed something")
    else:
        return HttpResponse(f"This was a {request.method} request")
