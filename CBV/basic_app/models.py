from django.db import models

class School(models.Model):
    name=models.CharField(max_length=20)
    principal=models.CharField(max_length=20)
    location=models.CharField(max_length=20)
    def __str__(self):
        return self.name
class Student(models.Model):
    name=models.CharField(max_length=20)
    age=models.PositiveIntegerField()
    school=models.ForeignKey(School,related_name="students")
    def __str__(self):
        return self.name
