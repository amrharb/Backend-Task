from asyncore import write
from urllib import response
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.conf import settings
from django.views import View
from .forms import CoursesForm as check_course_validation
import uuid
import json
DB = settings.DB_FILE
from db import readDB, writeDB
def create_course(body,id="-1"):
    if(id=="-1"):
        id=str(uuid.uuid1())
    nw_course={"id": id,"name":body["name"],"description":body["description"]}
    return nw_course
def find_course(id):
    data=readDB(filename=DB)
    for i in range(len(data)):
        if data[i]["id"] == id:
            return i
    return -1
class Course(View):
   def get(self, request, *args, **kwargs):
        data=readDB(filename=DB)
        response={"courses":data}
        return JsonResponse(data=response,status=200,safe=False)

   def post(self, request, *args, **kwargs):
        body=json.loads(request.body)
        course=create_course(body)
        check=check_course_validation(course)
        if not check.is_valid():
            return JsonResponse(data=json.loads(check.errors.as_json()), status=403)
        writeDB(obj=course,filename=DB)
        return JsonResponse(data=course,status=201,safe=False)

class SingleCourse(View):
    def get(self, request, *args, **kwargs):
        data=readDB(filename=DB)
        idx=find_course(kwargs["id"])
        if(idx!=-1):
            response={"course":data[idx]}
            return JsonResponse(data=response,status=200,safe=False)
        else:
            response={"course":"not found"}
            return JsonResponse(data=response,status=404,safe=False)

    def put(self, request, *args, **kwargs):
        body=json.loads(request.body)
        idx=find_course(kwargs["id"])
        if(idx!=-1):
            nw_course=create_course(body,kwargs["id"])
            check=check_course_validation(nw_course)
            if not check.is_valid():
                return JsonResponse(data=json.loads(check.errors.as_json()), status=403)
            writeDB(obj=nw_course,filename=DB,old=idx)
            return JsonResponse(data=nw_course,status=202,safe=False)
        else:
            response={"course": "not found"}
            return JsonResponse(data=response,status=404,safe=False)
    
    def delete(self, request, *args, **kwargs):
        idx=find_course(kwargs["id"])
        if(idx!=-1):
            writeDB(obj="delete",filename=DB,old=idx,delete=1)
            response={"result": "Mission completed"}
            return JsonResponse(data=response,status=202,safe=False)
        else:
            response={"course": "not found"}
            return JsonResponse(data=response,status=404,safe=False)