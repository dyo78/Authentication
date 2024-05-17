from django.http import JsonResponse
from django.views import View
from django.shortcuts import get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from .models import CustomUser
from rest_framework.exceptions import AuthenticationFailed
import json
import jwt,datetime
from rest_framework.response import Response
from django.contrib.auth.hashers import make_password


class CustomUserInfo(View):
    @csrf_exempt
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def get(self, request, id):
        user = get_object_or_404(CustomUser, id=id, is_deleted=False)
        user_data = {
            'id': user.id,
            'name': user.name,
            'phone': user.phone,
            'email': user.email,
            'is_deleted': user.is_deleted
        }
        return JsonResponse(user_data, status=200)

    def put(self, request, id):
        user = get_object_or_404(CustomUser, id=id, is_deleted=False)
        data = json.loads(request.body)
        user.name = data.get('name', user.name)
        user.phone = data.get('phone', user.phone)
        user.email = data.get('email', user.email)
        user.save()
        user_data = {
            'id': user.id,
            'name': user.name,
            'phone': user.phone,
            'email': user.email,
            'is_deleted': user.is_deleted
        }
        return JsonResponse(user_data, status=200)

    def patch(self, request, id):
        user = get_object_or_404(CustomUser, id=id, is_deleted=False)
        data = json.loads(request.body)
        user.name = data.get('name', user.name)
        user.phone = data.get('phone', user.phone)
        user.email = data.get('email', user.email)
        user.save()
        user_data = {
            'id': user.id,
            'name': user.name,
            'phone': user.phone,
            'email': user.email,
            'is_deleted': user.is_deleted
        }
        return JsonResponse(user_data, status=200)

    def delete(self, request, id):
        user = get_object_or_404(CustomUser, id=id, is_deleted=False)
        user.is_deleted = True  # soft delete
        user.save()
        return JsonResponse({"msg": "User removed successfully"}, status=204)

class UserDetail(View):
    @csrf_exempt
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def get(self, request):
        users = CustomUser.objects.filter(is_deleted=False)
        users_data = []
        for user in users:
            user_data = {
                'id': user.id,
                'name': user.name,
                'phone': user.phone,
                'email': user.email,
                'is_deleted': user.is_deleted
            }
            users_data.append(user_data)
        return JsonResponse(users_data, status=200, safe=False)

    def post(self, request):
        data = json.loads(request.body)
        user = CustomUser.objects.create(
            name=data['name'],
            phone=data['phone'],
            email=data['email'],
            is_deleted=False,
            password = make_password(data['password'])
        )
        user_data = {
            'id': user.id,
            'name': user.name,
            'phone': user.phone,
            'email': user.email,
            'is_deleted': user.is_deleted
        }
        return JsonResponse(user_data, status=201)

class DeletedUserDetail(View):
    @csrf_exempt
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def get(self, request):
        users = CustomUser.objects.filter(is_deleted=True)
        users_data = []
        for user in users:
            user_data = {
                'id': user.id,
                'name': user.name,
                'phone': user.phone,
                'email': user.email,
                'is_deleted': user.is_deleted
            }
            users_data.append(user_data)
        return JsonResponse(users_data, status=200, safe=False)
    
    def put(self, request, id): 
        user = get_object_or_404(CustomUser, id=id, is_deleted=True)  # get the user with id to restore
        user.is_deleted = False  # restore
        user.save()
        return JsonResponse({"msg": "User restored successfully"}, status=200)


class LoginView(View):
    @csrf_exempt
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def post(self,request):
        data = json.loads(request.body)
        email=data['email']
        password=data['password']

        user=CustomUser.objects.filter(email=email).first()

        if user is None:
            raise AuthenticationFailed('User not found')

        if not user.check_password(password):
            raise AuthenticationFailed('Incorrect Password!')


        access_token_payload={
            'id':user.id,
            'email':user.email,
            'exp':datetime.datetime.utcnow()+datetime.timedelta(minutes=1),
            'iat':datetime.datetime.utcnow(),
            'type':"access_type",

        }
        access_token=jwt.encode(access_token_payload,'secret',algorithm='HS512')

 
        refresh_token_payload={
            'id':user.id,
            'email':user.email,
            'exp':datetime.datetime.utcnow()+datetime.timedelta(days=30),
            'iat':datetime.datetime.utcnow(),
            'type':"refresh_type",
        }
        refresh_token=jwt.encode(refresh_token_payload,'secret',algorithm='HS512')
        response=JsonResponse({'access_token':access_token, 'refresh_token':refresh_token})

        response.set_cookie(key='jwt',value=access_token,httponly=True)

        response.set_cookie(key='refresh_token',value=refresh_token,httponly=True)

        return response

class UserView(View): 
    @csrf_exempt
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)


    def post(self,request):
        data = json.loads(request.body)
        email=data['email']
        password=data['password']

        user=CustomUser.objects.filter(email=email).first()

        if user is None:
            raise AuthenticationFailed('User not found')

        if not user.check_password(password):
            raise AuthenticationFailed('Incorrect Password!')


   
        access_token=request.COOKIES.get('jwt')
        refresh_token=request.COOKIES.get('refresh_token')


        time=datetime.datetime.now()
        newtime=int(time.timestamp())


        if not access_token:
            raise AuthenticationFailed('Unauthenticated')


        try:
            access_token_payload=jwt.decode(access_token,'secret',algorithms='HS512')

        except jwt.ExpiredSignatureError:
            refresh_token_payload=jwt.decode(refresh_token,'secret',algorithms='HS512')

            if newtime<refresh_token_payload['exp']:
                access_token_payload={
                'id':user.id,
                'email':user.email,
                'exp':datetime.datetime.utcnow()+datetime.timedelta(minutes=1),
                'iat':datetime.datetime.utcnow(),
                'type':"access_type",

                }
                access_token=jwt.encode(access_token_payload,'secret',algorithm='HS512')
                response=JsonResponse({'access_token':access_token})
                response.set_cookie(key='jwt',value=access_token,httponly=True)

                return response
            else:
                raise AuthenticationFailed("Expired")

        return JsonResponse(access_token_payload,safe=False)

        