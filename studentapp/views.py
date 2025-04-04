# students/views.py

from django.shortcuts import render, redirect, get_object_or_404
from .models import Student
from .forms import StudentForm

def home(request):
    students = Student.objects.all()
    return render(request, 'studentapp/home.html', {'students': students})

def add_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = StudentForm()
    return render(request, 'studentapp/add_student.html', {'form': form})

def update_student(request, pk):
    student = get_object_or_404(Student, pk=pk)
    form = StudentForm(request.POST or None, instance=student)
    if form.is_valid():
        form.save()
        return redirect('home')
    return render(request, 'studentapp/update_student.html', {'form': form})

def delete_student(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == 'POST':
        student.delete()
        return redirect('home')
    return render(request, 'studentapp/delete_student.html', {'student': student})
