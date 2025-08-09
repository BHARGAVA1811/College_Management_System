from django.shortcuts import render, redirect
from django.http import HttpResponse
from.models import Student, Faculty, Course, Attendance, Marks  
import hashlib


def home(request):
    return render(request,'college_app/home.html')

def student_list(request):
    students = Student.objects.all()
    return render(request,'college_app/student_list.html',{'students':students})

def faculty_list(request):
    faculties = Faculty.objects.all()
    return render(request,'college_app/faculty_list.html',{'faculties':faculties})

def course_list(request):
    courses = Course.objects.all()
    return render(request,'college_app/course_list.html',{'courses':courses})

def attendance_list(request):
    records = Attendance.objects.all()
    return render(request,'college_app/attendance_list.html',{'records':records})

def marks_list(request):
    marks = Marks.objects.all()
    return render(request,'college_app/marks_list.html',{'marks':marks})
