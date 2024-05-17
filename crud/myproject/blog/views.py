from django.shortcuts import render, get_object_or_404
from django.views import View
from .models import Blog, CustomUser
from django.http import JsonResponse
import json
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

@method_decorator(csrf_exempt, name='dispatch')
class BlogInfo(View):
    def get(self, request, id):
        blog = get_object_or_404(Blog, id=id)
        blog_data = {
            'id': blog.id,
            'title': blog.title,
            'desc': blog.desc,
            'author': blog.author.email,  
            'created_at': blog.created_at,
            'edited_at': blog.edited_at
        }
        return JsonResponse(blog_data, status=200)

    def put(self, request, id):
        blog = get_object_or_404(Blog, id=id)
        data = json.loads(request.body)
        blog.title = data.get('title', blog.title)
        blog.desc = data.get('desc', blog.desc)
        
        author_id = data.get('author')
        if author_id:
            author = get_object_or_404(CustomUser, id=author_id)
            blog.author = author

        blog.created_at = data.get('created_at', blog.created_at)
        blog.edited_at = data.get('edited_at', blog.edited_at)
        blog.save()

        blog_data = {
            'id': blog.id,
            'title': blog.title,
            'desc': blog.desc,
            'author': blog.author.email,  
            'created_at': blog.created_at,
            'edited_at': blog.edited_at
        }
        return JsonResponse(blog_data, status=200)

    def patch(self, request, id):
        blog = get_object_or_404(Blog, id=id)
        data = json.loads(request.body)
        blog.title = data.get('title', blog.title)
        blog.desc = data.get('desc', blog.desc)

        author_id = data.get('author')
        if author_id:
            author = get_object_or_404(CustomUser, id=author_id)
            blog.author = author

        blog.created_at = data.get('created_at', blog.created_at)
        blog.edited_at = data.get('edited_at', blog.edited_at)
        blog.save()

        blog_data = {
            'id': blog.id,
            'title': blog.title,
            'desc': blog.desc,
            'author': blog.author.email,  
            'created_at': blog.created_at,
            'edited_at': blog.edited_at
        }
        return JsonResponse(blog_data, status=200)

    def delete(self, request, id):
        blog = get_object_or_404(Blog, id=id)
        blog.delete()
        return JsonResponse({"msg": "blog removed successfully"}, status=204)


@method_decorator(csrf_exempt, name='dispatch')
class BlogDetail(View):
    def get(self, request):
        blogs = Blog.objects.all()
        blogs_data = []
        for blog in blogs:
            blog_data = {
                'id': blog.id,
                'title': blog.title,
                'desc': blog.desc,
                'author': blog.author.email,  
                'created_at': blog.created_at,
                'edited_at': blog.edited_at,
                'is_deleted': blog.is_deleted
            }
            blogs_data.append(blog_data)
        return JsonResponse(blogs_data, status=200, safe=False)

    def post(self, request):
        data = json.loads(request.body)
        
        author_id = data.get('author')
        author = get_object_or_404(CustomUser, id=author_id)

        blog = Blog.objects.create(
            title=data['title'],
            desc=data['desc'],
            author=author 
        )

        blog_data = {
            'id': blog.id,
            'title': blog.title,
            'desc': blog.desc,
            'author': blog.author.email,  
            'created_at': blog.created_at,
            'edited_at': blog.edited_at
        }
        return JsonResponse(blog_data, status=201)
