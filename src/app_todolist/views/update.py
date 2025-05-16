from contextlib import contextmanager
from django.shortcuts import render, redirect
from app_blog.utility import query

def view(request, id):
    
    post = query("SELECT * FROM todolist_post WHERE id_task = %s", [id])
    print(post)
    
    if not post:
        return render(request, 'app_todolist/notfound.html', status=404)
    
    post = post[0]
        
    if request.method == 'POST':
        taskName = request.POST.get('taskName')
        taskDeadline = request.POST.get('taskDeadline')
        taskDetail = request.POST.get('taskDetail')
        
        query("UPDATE todolist_post SET task_name = %s, task_deadline = %s, task_detail = %s WHERE id_task = %s", [taskName, taskDeadline, taskDetail, id])
        
        return redirect(f"/blog/read/{id}")
    
    return render(request, "app_todolist/update.html", {"post": post})