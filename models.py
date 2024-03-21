from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class StudentId(models.Model):
    student_id = models.CharField(max_length=100)

    def __str__(self):
        return self.student_id


class Student(models.Model):
    user = models.ForeignKey(User , on_delete=models.SET_NULL,null=True,blank=True)
    # student_id = models.OneToOneField(StudentId,related_name='studentid',on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    rollno = models.IntegerField(default=9999)
    branch = models.CharField(max_length=30,default="none")
    email = models.CharField(max_length=30,default="none",primary_key=True)
    phone = models.BigIntegerField(default=9999)


class Subject(models.Model):
    subject_name = models.CharField(max_length=30 ,default='Stu-001')

    def __str__(self):
        return self.subject_name

class student_Marks(models.Model):
    student = models.ForeignKey(Student ,related_name="student", on_delete=models.CASCADE )
    subject = models.ForeignKey(Subject, related_name="subject", on_delete=models.CASCADE)
    marks= models.IntegerField()

    def __str__(self):
        return f"{self.student.name} {self.subject.subject_name}"

    class Meta:
        unique_together =['student','subject']


