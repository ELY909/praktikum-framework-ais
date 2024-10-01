from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import StudentsForm
from .models import Students

def homepage(request):
    return render(request, 'homepage/index.html')

def about(request):
    return render(request, 'homepage/about.html')


def student_index(request):
    students = Students.objects.all()
    return render(request, 'student/index.html', {'students': students})

def student_create(request):
    if request.method == 'POST':
        form = StudentsForm(request.POST)
        if form.is_valid():
            form.save()  
            messages.success(request, 'Mahasiswa berhasil dibuat!')  
            return redirect('student_index') 
    else:
        form = StudentsForm()
    return render(request, 'student/create.html', {'form': form})
