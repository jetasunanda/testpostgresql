from django.shortcuts import render, redirect
from app_todolist.utility import query

def view(request, id):

    if request.method == 'GET':
        post = query("SELECT * FROM todolist_post WHERE id_task = %s", [id])
        print(post)
        
        if not post:
            return render(request, 'app_todolist/notfound.html', status=404)
        
        post = query("DELETE FROM todolist_post WHERE id_task = %s", [id])
    
    return redirect("/todo/list/", name="todolist_list")