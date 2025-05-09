'''
id didapat url yang dimasukan oleh user.
post = query("SELECT * FROM blog_post WHERE id = %s", [id])

tuliskan logic co de untuk melakukan render post yang ditemukan ke
frontend atau html

Jika tidak 
'''

from django.shortcuts import render
from app_blog.utility import query

def view(request, id):
    
    if request.method == 'GET':
        post = query("SELECT * FROM blog_post WHERE id = %s", [id])
        if post:
            return render(request, 'app_blog/read.html', {
            'post': post[0]
        })
    
        return render(request, 'app_blog/notfound.html', status=404)
    
    