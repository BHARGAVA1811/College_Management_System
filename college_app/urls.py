from django.contrib import admin
from django.urls import path
from.import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('students/', views.student_list, name='student_list'),
    path('faculties/', views.faculty_list, name='faculty_list'),
    path('courses/', views.course_list, name='course_list'),
    path('attendance/', views.attendance_list, name='attendance_list'),
    path('marks/', views.marks_list, name='marks_list'),
]
