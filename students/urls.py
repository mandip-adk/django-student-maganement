from django.urls import path
from . import views

urlpatterns=[
    path('students/',views.student_list, name='student_list'),
    path('students/<int:rollno>/',views.student_detail, name='student_detail'),
    path('students/add/', views.add_student, name='add_student'),
    
]