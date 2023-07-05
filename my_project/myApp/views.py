from django.shortcuts import render, get_object_or_404, redirect
from .models import Course
from .models import Student

def student_list(request):
    students = Student.objects.all()
    return render(request, 'student_list.html', {'students': students})

def student_add(request):
    if request.method == 'POST':
        name = request.POST['name']
        course_id = request.POST['course']
        student = Student.objects.create(name=name, course_id=course_id)
        return redirect('student_list')
    else:
        courses = Course.objects.all()
        return render(request, 'student_add.html', {'courses': courses})

def student_edit(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == 'POST':
        student.name = request.POST['name']
        student.course_id = request.POST['course']
        student.save()
        return redirect('student_list')
    else:
        courses = Course.objects.all()
        return render(request, 'student_edit.html', {'student': student, 'courses': courses})

def student_delete(request, pk):
    student = get_object_or_404(Student, pk=pk)
    student.delete()
    return redirect('student_list')
