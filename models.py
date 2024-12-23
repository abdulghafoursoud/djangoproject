from django.db import models

class Student(models.Model):
    student_name = models.CharField(max_length=20)
    age = models.IntegerField()
    academic_year = models.CharField(max_length=10)
    year_study = models.CharField(max_length=10)
    phone_number = models.BigIntegerField()
    course_name = models.CharField(max_length=30)
    reg_no = models.CharField(max_length=20, unique=True)
    gender = models.CharField(max_length=10)
    password = models.CharField(max_length=100)
    email = models.EmailField(max_length=254,unique=True)

    def __str__(self):
        return f"{self.student_name}"
    
class Instructor(models.Model):
    name = models.CharField(max_length=20)
    password = models.CharField(max_length=100)
    email = models.EmailField(max_length=254,unique=True)
    
    def __str__(self):
        return f"{self.name}"
    
class Project(models.Model):
    student_name = models.CharField(max_length=100)
    project_title = models.CharField(max_length=100)
    st_reg_no = models.CharField(max_length=100)
    date_uploaded = models.DateField(auto_now_add=True)
    student = models.OneToOneField(Student,on_delete=models.CASCADE)
    project_file = models.FileField(upload_to='projects/')

    def __str__(self):
        return f"{self.student_name}"
    
class Admin(models.Model):
    password = models.CharField(max_length=100)
    email = models.EmailField(max_length=254,unique=True)
    
    def __str__(self):
        return f"{self.email}"
    
