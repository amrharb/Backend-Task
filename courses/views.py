from asyncore import write
from urllib import response
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.conf import settings
from django.views import View
from .forms import CoursesForm as check_course_validation
from .models import Course as CourseQuery
import json

def create_Course(body):
    return CourseQuery.objects.create(
        name=body["name"],
        description=body["description"])

def update_Course(body,userId):
    CourseQuery.objects.filter(id=userId).update(
        name=body["name"],
        description=body["description"])

def convert_to_Json(body):
    jsonData=[]
    for i in range(len(body)):
        jsonData.append({
        "name":body[i].name,
        "description":body[i].description})
    return jsonData
class Course(View):
   def get(self, request, *args, **kwargs):
        courses=CourseQuery.objects.all()
        if(len(courses)==0):
            return JsonResponse(data={"result":"courses not found"},status=404,safe=False)
        else:
            return JsonResponse(data=convert_to_Json(courses),status=200,safe=False)

   def post(self, request, *args, **kwargs):
        body=json.loads(request.body)
        course=create_Course(body)
        check=check_course_validation(body)
        if not check.is_valid():
            return JsonResponse(data=json.loads(check.errors.as_json()), status=403)
        return JsonResponse(data=convert_to_Json([course]),status=201,safe=False)

class SingleCourse(View):
    def get(self, request, *args, **kwargs):
         nw_course=CourseQuery.objects.filter(id=kwargs["id"])
         if(len(nw_course)==0):
            return JsonResponse(data={"result":"user not found"},status=404,safe=False)
         return JsonResponse(data=convert_to_Json([CourseQuery.objects.get(pk=kwargs["id"])]),status=202,safe=False)

    def put(self, request, *args, **kwargs):
        course=CourseQuery.objects.filter(id=kwargs["id"])
        if(len(course)==0):
            return JsonResponse(data={"result":"user not found"},status=404,safe=False)
        body=json.loads(request.body)
        check=check_course_validation(body)
        if not check.is_valid():
            return JsonResponse(data=json.loads(check.errors.as_json()), status=403)
        update_Course(body,kwargs["id"])
        return JsonResponse(data=body,status=200,safe=False)

    def delete(self, request, *args, **kwargs):
        course=CourseQuery.objects.filter(pk=kwargs["id"])
        if(len(course)==0):
            return JsonResponse(data={"result":"course not found"},status=404,safe=False)
        CourseQuery.objects.get(pk=kwargs["id"]).delete()
        return JsonResponse(data={"result":"mission completed"},status=200,safe=False)