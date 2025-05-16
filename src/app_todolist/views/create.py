from django.shortcuts import render
from app_todolist.utility import query
# ini menggunakan django raw query

def view(request):
    if request.method == 'POST':
        taskName = request.POST.get('taskName')
        taskDeadline = request.POST.get('taskDeadline')
        taskDetail = request.POST.get('taskDetail')

        result = query("INSERT INTO todolist_post (task_name, task_deadline, task_detail) VALUES (%s, %s, %s)", [taskName, taskDeadline, taskDetail])
        print(result)

    return render(request, 'app_todolist/create.html')