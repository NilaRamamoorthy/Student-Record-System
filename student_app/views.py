
from django.shortcuts import render, redirect, get_object_or_404
from .models import Student
from .forms import StudentForm

def student_list(request):
    students = Student.objects.all()
    return render(request, 'student_app/student_list.html', {'students': students})

def student_detail(request, id):
    student = get_object_or_404(Student, pk=id)
    return render(request, 'student_app/student_detail.html', {'student': student})

def student_create(request):
    form = StudentForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('student_list')
    return render(request, 'student_app/student_form.html', {'form': form})

def student_edit(request, id):
    student = get_object_or_404(Student, pk=id)
    form = StudentForm(request.POST or None, instance=student)
    if form.is_valid():
        form.save()
        return redirect('student_list')
    return render(request, 'student_app/student_form.html', {'form': form})

def student_delete(request, id):
    student = get_object_or_404(Student, pk=id)
    if request.method == 'POST':
        student.delete()
        return redirect('student_list')
    return render(request, 'student_app/student_detail.html', {'student': student})
