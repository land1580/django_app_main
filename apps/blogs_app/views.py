from django.shortcuts import render, HttpResponse, redirect

def index(request): # Main route
    response = "placeholder to later display all the list of blogs"
    return HttpResponse(response) # displays msg on page

def new(request): # "New" route
    response = "placeholder to display a new form to create a new blog"
    return HttpResponse(response) # displays msg on page

def create(request): # "Create" route
    return redirect("/") # goes back to main route

def show(request, number): # "Show" route
    print(number) # displays num in terminal
    return HttpResponse("placeholder to display blog " + number) # displays msg & num on page

def edit(request, number): # "Edit" route
    print(number) # displays num in terminal
    return HttpResponse("placeholder to edit blog " + number) # displays msg & num on page

def destroy(request, number): # "Destroy" route
    print(number) # displays num in terminal
    return redirect("/") # goes back to main route