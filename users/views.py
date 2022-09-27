from django.shortcuts import render
from django.views import View
from django.http import JsonResponse,HttpResponse
from .models import User as UserQuery
from django.conf import settings
from .forms import UsersForm as check_user_validation
import json
def create_User(body):
    return UserQuery(
        first_name=body["first_name"],
        last_name=body["last_name"],
        birth_date=body["birth_date"],
        email=body["email"],
        password=body["password"],)

def update_User(body,userId):
    UserQuery.objects.filter(id=userId).update(
        first_name=body["first_name"],
        last_name=body["last_name"],
        birth_date=body["birth_date"],
        email=body["email"],
        password=body["password"],)
def convert_to_Json(body):
    jsonData=[]
    for i in range(len(body)):
        jsonData.append({
        "first_name":body[i].first_name,
        "last_name":body[i].last_name,
        "birth_date":body[i].birth_date,
        "email":body[i].email,
        "password":body[i].password})
    return jsonData

def get_users(age):
    users=UserQuery.objects.all()
    user=[]
    for i in range(len(users)):
        if(users[i].age>=age):
            user.append(users[i])
    return users

class User(View):
    def get(self, request, *args, **kwargs):
        users=UserQuery.objects.all()
        if(len(users)==0):
            return JsonResponse(data={"result":"users not found"},status=404,safe=False)
        else:
            return JsonResponse(data=convert_to_Json(users),status=200,safe=False)
        
    def post(self, request, *args, **kwargs):
        body=json.loads(request.body)
        nw_user=create_User(body)
        check=check_user_validation(body)
        if not check.is_valid() and not nw_user.is_valid():
            return JsonResponse(data=json.loads(check.errors.as_json()), status=403)
        return JsonResponse(data=convert_to_Json([nw_user]),status=201,safe=False)


class Comp_Users(View):
    def get(self, request, *args, **kwargs):
        users=get_users(kwargs["age"])
        # users=UserQuery.objects.all().filter(age__gte=kwargs["age"])
        if(len(users)==0):
            return JsonResponse(data={"result":"users not found"},status=404,safe=False)
        return JsonResponse(data=convert_to_Json(users),status=202,safe=False)
        
class SingleUser(View):
    def get(self, request, *args, **kwargs):
        nw_user=UserQuery.objects.filter(id=kwargs["id"])
        if(len(nw_user)==0):
            return JsonResponse(data={"result":"user not found"},status=404,safe=False)
        return JsonResponse(data=convert_to_Json([UserQuery.objects.get(pk=kwargs["id"])]),status=202,safe=False)
    
    def put(self, request, *args, **kwargs):
        user=UserQuery.objects.filter(id=kwargs["id"])
        if(len(user)==0):
            return JsonResponse(data={"result":"user not found"},status=404,safe=False)
        body=json.loads(request.body)
        check=check_user_validation(body)
        if not check.is_valid():
            return JsonResponse(data=json.loads(check.errors.as_json()), status=403)
        update_User(body,kwargs["id"])
        return JsonResponse(data=body,status=200,safe=False)


    def delete(self, request, *args, **kwargs):
        user=UserQuery.objects.filter(pk=kwargs["id"])
        if(len(user)==0):
            return JsonResponse(data={"result":"user not found"},status=404,safe=False)
        UserQuery.objects.get(pk=kwargs["id"]).delete()
        return JsonResponse(data={"result":"mission completed"},status=200,safe=False)