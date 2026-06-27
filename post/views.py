from django.shortcuts import render
from django.http import HttpResponse, Http404
import json
import os
current_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(current_dir, 'data.txt')

with open(file_path, 'r') as file:
    posts = json.load(file)

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