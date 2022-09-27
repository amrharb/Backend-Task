from enum import unique
from django.db import models

class Course(models.Model):
    name = models.CharField(max_length=20,unique=True)
    description = models.TextField()

    class Meta:
        db_table='course'   # rename table for Course_course to coure
        ordering=['name','-description']
    
    def __str__(self):
        return '{}'.format(self.name)