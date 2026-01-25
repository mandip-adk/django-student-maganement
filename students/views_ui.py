from django.shortcuts import render,redirect, get_object_or_404
from .models import Student

def student_list_ui(request):
    students = Student.objects.all()
    return render(request, "students/student_listui.html", {
        "students": students
    })

def add_student_ui(request):
    if request.method == "POST":
        name = request.POST.get("name")
        rollno = request.POST.get("rollno")
        stu_class = request.POST.get("stu_class")
        section = request.POST.get("section")
        marks = request.POST.get("marks")
        address = request.POST.get("address")

        Student.objects.create(
            name=name,
            rollno=rollno,
            stu_class=stu_class,
            section=section,
            marks=marks,
            address=address
        )

        return redirect("student_list_ui")

    return render(request, "students/add_studentui.html")

def delete_student_ui(request, student_id):
    student = get_object_or_404(Student, id=student_id)

    if request.method == "POST":
        student.delete()
        return redirect("student_list_ui")

    return render(request, "students/delete_studentui.html", {
        "student": student
    })

def update_student_ui(request, student_id):
    student = get_object_or_404(Student, id=student_id)

    if request.method == "POST":
        student.name = request.POST.get("name")
        student.rollno = request.POST.get("rollno")
        student.stu_class = request.POST.get("stu_class")
        student.section = request.POST.get("section")
        student.marks = request.POST.get("marks")
        student.address = request.POST.get("address")

        student.save()
        return redirect("student_list_ui")

    return render(request, "students/update_studentui.html", {
        "student": student
    })