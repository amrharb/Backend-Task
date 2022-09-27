from enum import unique
from wsgiref import validate
from django.db import models
import datetime
from django.core.exceptions import ValidationError
# Create your models here.

def validate_email(UserEmail):
    if User.objects.filter(email=UserEmail).exists():
            raise ValidationError(("Email already exists"),
            code="not_unique",
        )
    return UserEmail
class User(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    birth_date = models.DateField(max_length=8)
    email = models.EmailField(max_length=30, unique=True)
    password = models.TextField()

    class Meta:
        db_table='user'   # rename table for Course_course to coure
        ordering=['first_name','last_name']
    
    def __str__(self):
        return '{}'.format(self.name)

    @property
    def name(self):
        return '{} {}'.format(self.first_name,self.last_name)
    

    @property
    def age(self):
       current_time = datetime.datetime.now()
       return (current_time.year-self.birth_date.year)