from django.shortcuts import render
from django.http import HttpResponse, Http404

posts = [
    {
        "id": 1,
        "title": "Introduction to Python",
        "content": "Python is a versatile programming language used for web development, data science, automation, and more."
    },
    {
        "id": 2,
        "title": "Understanding Lists",
        "content": "Lists are ordered collections in Python that can store multiple items."
    },
    {
        "id": 3,
        "title": "Working with Dictionaries",
        "content": "Dictionaries store data as key-value pairs and provide fast lookups."
    },
    {
        "id": 4,
        "title": "Getting Started with Flask",
        "content": "Flask is a lightweight Python web framework used to build web applications."
    },
    {
        "id": 5,
        "title": "REST API Basics",
        "content": "A REST API allows communication between clients and servers using HTTP methods."
    }
]

def home(request):
    # Pass the entire list of dictionaries to the template
    context = {'posts': posts}
    return render(request, 'post/home.html', context)


def dynamic_view(request, id):
    # 1. Search for the specific post
    selected_post = None
    for post in posts:
        if post["id"] == id:
            selected_post = post
            break
            
    # 2. If no post is found, show a standard 404 error
    if selected_post is None:
        raise Http404("Post not found")
        
    # 3. If found, package it up and send it to the template!
    context = {'post': selected_post}
    return render(request, 'post/post.html', context)