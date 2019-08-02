from django.db import models

# Create your models here.
# login/models.py


class User(models.Model):
    gender = (
        ('male', '男'),
        ('female', '女'),
    )
    name = models.CharField(max_length=128,unique=True)
    password = models.CharField(max_length=256)
    email = models.EmailField(unique=True)
    sex = models.CharField(max_length=32, choices=gender, default='男')
    c_time = models.DateTimeField(auto_now_add=True)
    c_kind = models.CharField(max_length=128, default='普通用户')

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['c_time']
        verbose_name = '用户'
        verbose_name_plural = '用户'


class Grade(models.Model):
    id = models.AutoField(primary_key=True, max_length=255)
    student_id = models.CharField(max_length=255)
    class_id = models.CharField(max_length=255)
    class_name = models.CharField(max_length=255)
    grade = models.CharField(max_length=255)
    grade_point = models.DecimalField(max_digits=2, decimal_places=1, blank=True, null=True)


class RetrieveQuestion(models.Model):
    name = models.CharField(primary_key=True, max_length=128)
    question_1 = models.CharField(max_length=255, blank=True)
    question_2 = models.CharField(max_length=255, blank=True)
    question_3 = models.CharField(max_length=255, blank=True)
    answer_1 = models.CharField(max_length=255, blank=True)
    answer_2 = models.CharField(max_length=255, blank=True)
    answer_3 = models.CharField(max_length=255, blank=True)


class Student(models.Model):
    student_id = models.CharField(primary_key=True, max_length=255)
    student_name = models.CharField(max_length=128)
    gender = models.IntegerField()
    age = models.IntegerField()
    birth = models.DateTimeField(max_length=6)




