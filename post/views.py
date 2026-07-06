from django.shortcuts import render, redirect,get_object_or_404
from django.http import HttpResponse, Http404
from .models import Post



def home(request):
    posts = Post.objects.all() 
    return render(request, 'post/home.html', {'posts': posts})


def dynamic_view(request, id):

    selected_post = get_object_or_404(Post, id=id)        
    # Package the found post into a dictionary
    context = {'post': selected_post}
    return render(request, 'post/post.html', context)



def create_post(request):
    # Check if the user is submitting the form
    if request.method == 'POST':
        # Extract the data from the HTML form using the 'name' attributes
        title = request.POST.get('title')
        content = request.POST.get('content')
        
        # Save it to the database if both fields are filled
        if title and content:
            Post.objects.create(title=title, content=content)
            return redirect('home')
        
    return render(request, 'post/create_post.html')


def delete_post(request, id):
    post_to_delete = get_object_or_404(Post, id=id)
    
    if request.method == 'POST':
        post_to_delete.delete()
        
    return redirect('home')



def update_post(request, id):
    # Get the specific post to edit
    post = get_object_or_404(Post, id=id)
    
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        
        # Ensure fields aren't empty, then update and save
        if title and content:
            post.title = title
            post.content = content
            post.save()
            return redirect('home')
            
    # If it's a GET request, pass the post to the template to pre-fill the form
    return render(request, 'post/update_post.html', {'post': post})