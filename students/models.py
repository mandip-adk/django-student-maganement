from django.db import models

class Student(models.Model):
    
    name= models.CharField(max_length=100)
    
    stu_class= models.IntegerField()
    rollno= models.IntegerField(unique=True)
    section= models.CharField(max_length=10)
    marks= models.IntegerField()
    address= models.CharField(max_length=100)
    
    def __str__(self):
        return f"{self.rollno}. {self.name}"
    