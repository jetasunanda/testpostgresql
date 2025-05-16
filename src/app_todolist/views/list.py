from django.shortcuts import render
from app_blog.utility import query

def view(request):
    
    if request.method == 'GET':
        posts = query("SELECT * FROM todolist_post")
    return render(request, 'app_todolist/list.html', {
        'posts': posts
    })
    