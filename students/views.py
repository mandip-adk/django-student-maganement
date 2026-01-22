from django.shortcuts import render, get_object_or_404, redirect
from . models import Student

def student_list(request):
    rollno = request.GET.get('rollno')

    if rollno:
        students = Student.objects.filter(rollno=rollno)
    else:
        students = Student.objects.all()
    return render(request, 'students/student_list.html',{
        'students': students
    })

def student_detail(request,rollno):
    student = get_object_or_404(Student, rollno=rollno)
    return render(request,'students/student_details.html',{
        'student':student
    })

def add_student(request):
    if request.method == "POST":
        name = request.POST.get('name')
        address = request.POST.get('address')
        stu_class = request.POST.get('stu_class')
        rollno = request.POST.get('rollno')
        section = request.POST.get('section')
        marks = request.POST.get('marks')

#Duplicate rollno check
        if Student.objects.filter(rollno=rollno).exists():
            return render(request, 'students/add_student.html',{
                'error':'Roll number already exists...'
            })
        
    #save to database
        Student.objects.create(
            name=name,
            address=address,
            stu_class=stu_class,
            rollno=rollno,
            section=section,
            marks=marks,
        )

        return redirect('/students/')

    return render(request,'students/add_student.html')
