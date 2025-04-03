from django.db import models

class Student(models.Model):
    student_key = models.PositiveIntegerField(primary_key=True)
    roll_no = models.CharField(max_length=45, unique=True, null=True)
    name = models.CharField(max_length=45, null=True)
    age = models.PositiveIntegerField(null=True)
    gender = models.SmallIntegerField(null=True)

    class Meta:
        managed = False  # Prevents Django from managing the table schema
        db_table = 'students'  # Matches the existing table name