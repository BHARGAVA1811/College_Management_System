from django.db import models 


class Student(models.Model):
    name = models.CharField(max_length=100)
    admission_no = models.CharField(max_length=20, unique=True)
    dob = models.DateField()
    department = models.CharField(max_length=100)
     
    def __str__(self):
        return self.name



class Faculty(models.Model):
    name = models.CharField(max_length=100)
    department = models.CharField(max_length=100)
    contact_no = models.CharField(max_length=16)
    
    def __str__(self):
        return self.name



class Course(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=20)
    faculty = models.ManyToManyField(Faculty, blank=True)
    students = models.ManyToManyField(Student, blank=True)
    
    def __str__(self):
        return self.name
    

    

class Attendance(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    date = models.DateField()
    status = models.CharField(max_length=10,choices=[('Present', 'Present'), ('Absent', 'Absent')])

    def __str__(self):
        return f"{self.student.name}   {self.status}  "


class Exam(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    date = models.DateField()
    max_marks = models.IntegerField()

    def __str__(self):
        return f"{self.course.name}"


class Marks(models.Model):
   student = models.ForeignKey(Student, on_delete=models.CASCADE)
   exam = models.ForeignKey(Exam, on_delete=models.CASCADE)
   marks = models.IntegerField()


   def __str__(self):
        return f"{self.student.name}  scored {self.marks} in{self.exam.course} "

