from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from .models import Student
from .forms import StudentForm, UserForm
from django.db import IntegrityError
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages

# Create your views here.
def index(request):
      search = request.GET.get('search')
      if search:
            students = Student.objects.filter(first_name__icontains=search)
            return render(request, 'students/index.html', {'students': students})
      else:
            return render(request, 'students/index.html', {'students': Student.objects.all()})

def index2(request):
      search = request.GET.get('search')
      if search:
            students = Student.objects.filter(first_name__icontains=search)
            return render(request, 'students/index2.html', {'students': students})
      else:
            return render(request, 'students/index2.html', {'students': Student.objects.all()})

def user_signup(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return HttpResponseRedirect(reverse('index'))
    else:
        form = UserForm()
    return render(request, 'students/signup.html', {'form': form})

def view_student(request, id):
  return HttpResponseRedirect(reverse('index'))

def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'Login successful.')
            return HttpResponseRedirect(reverse('index'))
        else:
            messages.error(request, 'Invalid login credentials.')
    return render(request, 'students/login.html')

def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('login'))
    

def add(request):
  if request.method == 'POST':
    form = StudentForm(request.POST)
    if form.is_valid():
      new_student_number = form.cleaned_data['student_number']
      new_first_name = form.cleaned_data['first_name']
      new_last_name = form.cleaned_data['last_name']
      new_email = form.cleaned_data['email']
      new_field_of_study = form.cleaned_data['field_of_study']
      new_gpa = form.cleaned_data['gpa']

      new_student = Student(
        student_number=new_student_number,
        first_name=new_first_name,
        last_name=new_last_name,
        email=new_email,
        field_of_study=new_field_of_study,
        gpa=new_gpa
      )
      new_student.save()
      return render(request, 'students/add.html', {
        'form': StudentForm(),
        'success': True
      })
  else:
    form = StudentForm()
  return render(request, 'students/add.html', {
    'form': StudentForm()
  })


def edit(request, id):
  if request.method == 'POST':
    student = Student.objects.get(pk=id)
    form = StudentForm(request.POST, instance=student)
    if form.is_valid():
      form.save()
      return render(request, 'students/edit.html', {
        'form': form,
        'success': True
      })
  else:
    student = Student.objects.get(pk=id)
    form = StudentForm(instance=student)
  return render(request, 'students/edit.html', {
    'form': form
  })


def delete(request, id):
  if request.method == 'POST':
    student = Student.objects.get(pk=id)
    student.delete()
  return HttpResponseRedirect(reverse('index'))
