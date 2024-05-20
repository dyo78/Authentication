from django.http import JsonResponse
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from blog.models import Blog
from django.shortcuts import get_object_or_404
from myapp.models import CustomUser
import jwt
from functools import wraps
from django.utils.decorators import method_decorator
import json

def login_and_permission_required(view_func):
    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):
        auth_header = request.headers.get('Authorization')

        if not auth_header:
            return JsonResponse({'error': 'Authorization header missing'}, status=401)

        try:
            token = auth_header.split(' ')[1]
            access_token_payload = jwt.decode(token, 'secret', algorithms='HS256')
            request.user_id = access_token_payload['id']
            request.user = CustomUser.objects.get(pk=request.user_id)
        except (jwt.exceptions.DecodeError, jwt.exceptions.ExpiredSignatureError, jwt.exceptions.InvalidTokenError):
            return JsonResponse({'error': 'Invalid or expired token'}, status=401)
        except CustomUser.DoesNotExist:
            return JsonResponse({'error': 'User not found'}, status=404)

        blog_id = kwargs.get('pk')
        if blog_id:
            blog = get_object_or_404(Blog, id=blog_id)
            if blog.author.id != request.user_id:
                return JsonResponse({'error': 'Unauthorized access to blog'}, status=403)

        return view_func(request, *args, **kwargs)

    return _wrapped_view

class BlogDetail(View):
    @method_decorator(csrf_exempt)
    @method_decorator(login_and_permission_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def get(self, request):
        blogs = Blog.objects.filter(is_deleted=False)
        blog_data = [{'id': blog.id,
                      'title': blog.title,
                      'desc': blog.desc,
                      'created_at': blog.created_at,
                      'edited_at': blog.edited_at,
                      'author': blog.author.email if blog.author else 'Unknown'} for blog in blogs]
        return JsonResponse(blog_data, safe=False)

    def post(self, request):
        blog_data = json.loads(request.body)
        try:
            blog = Blog.objects.create(title=blog_data['title'],
                                       desc=blog_data['desc'],
                                       author=request.user)
            return JsonResponse({'id': blog.id,
                                 'title': blog.title,
                                 'desc': blog.desc,
                                 'created_at': blog.created_at,
                                 'edited_at': blog.edited_at,
                                 'author': request.user.email}, status=201)
        except KeyError:
            return JsonResponse({'error': 'Invalid data provided'}, status=400)

class BlogInfo(View):
    @method_decorator(csrf_exempt)
    @method_decorator(login_and_permission_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def get(self, request, pk=None):
        if pk:
            blog = get_object_or_404(Blog, id=pk, is_deleted=False)
            blog_data = {'id': blog.id, 'title': blog.title,
                         'desc': blog.desc,
                         'created_at': blog.created_at,
                         'edited_at': blog.edited_at,
                         'author': blog.author.email if blog.author else 'Unknown'}
            return JsonResponse(blog_data)
        else:
            blogs = Blog.objects.filter(author=request.user, is_deleted=False)
            blog_data = [{'id': blog.id,
                          'title': blog.title,
                          'desc': blog.desc,
                          'created_at': blog.created_at,
                          'edited_at': blog.edited_at,
                          'author': blog.author.email if blog.author else 'Unknown'} for blog in blogs]
            return JsonResponse(blog_data, safe=False)

    def put(self, request, pk):
        blog_data = json.loads(request.body)
        try:
            blog = get_object_or_404(Blog, id=pk, author=request.user)
            blog.title = blog_data['title']
            blog.desc = blog_data['desc']
            blog.save()
            return JsonResponse({'id': blog.id, 'title': blog.title,
                                 'desc': blog.desc,
                                 'created_at': blog.created_at,
                                 'edited_at': blog.edited_at,
                                 'author': blog.author.email if blog.author else 'Unknown'})
        except KeyError:
            return JsonResponse({'error': 'Invalid data provided'}, status=400)

    def patch(self, request, pk):
        blog_data = json.loads(request.body)
        try:
            blog = get_object_or_404(Blog, id=pk, author=request.user)
            if 'title' in blog_data:
                blog.title = blog_data['title']
            if 'desc' in blog_data:
                blog.desc = blog_data['desc']
            if 'edited_at' in blog_data:
                blog.edited_at = blog_data['edited_at']
            blog.save()
            return JsonResponse({'id': blog.id, 'title': blog.title,
                                 'desc': blog.desc,
                                 'created_at': blog.created_at,
                                 'edited_at': blog.edited_at,
                                 'author': blog.author.email if blog.author else 'Unknown'})
        except KeyError:
            return JsonResponse({'error': 'Invalid data provided'}, status=400)

    def delete(self, request, pk):
        try:
            blog = get_object_or_404(Blog, id=pk, author=request.user)
            blog.delete()
            return JsonResponse({'message': 'Blog deleted'}, status=204)
        except Blog.DoesNotExist:
            return JsonResponse({'error': 'Blog not found'}, status=404)
