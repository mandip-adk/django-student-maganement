from django import forms
from .models import Student

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name','address','stu_class','rollno','section','marks']
        error_message = {
            'rollno':{
                'unique':'This roll number is already assigned.'
            }
        }
        