from django.urls import path
from .views import *

urlpatterns=[
    path("", User.as_view()), 
    path("<int:id>", SingleUser.as_view()),
    path("age<int:age>", Comp_Users.as_view())
]