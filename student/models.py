from django.db import models

# Create your models here.
class Student(models.Model):
    student_key = models.AutoField(primary_key=True)
    roll_no = models.CharField(max_length=45, unique=True)
    name = models.CharField(max_length=45)
    age = models.PositiveIntegerField(null=True, blank=True)
    gender = models.BooleanField(null=True, blank=True)  # True for Male, False for Female

    def __str__(self):
        return self.name