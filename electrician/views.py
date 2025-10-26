from django.shortcuts import render
from django.http import HttpResponse


def contacts(request) -> HttpResponse:
    return render(request, "electrician/contacts.html")

def about_us(request) -> HttpResponse:
    return render(request, "electrician/about_us.html")

def main(request) -> HttpResponse:
    return render(request, "electrician/main.html")

def create_project(request) -> HttpResponse:
    if request.method == "GET":
        return render(request, "electrician/create_project.html")
    elif request.method == "POST":
        pass



