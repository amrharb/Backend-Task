from django.urls import path
from .views import *
urlpatterns=[
    path("", Course.as_view()), 
    path("<int:id>", SingleCourse.as_view())
]