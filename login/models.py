# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Grades(models.Model):
    student_id = models.CharField(max_length=255)
    class_id = models.CharField(max_length=255)
    class_name = models.CharField(max_length=255)
    grade = models.CharField(max_length=255)
    grade_point = models.DecimalField(max_digits=2, decimal_places=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'grades'


class Logs(models.Model):
    name = models.CharField(max_length=128, blank=True, null=True)
    operation = models.CharField(max_length=255, blank=True, null=True)
    time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'logs'


class RetrieveQuestions(models.Model):
    name = models.CharField(primary_key=True, max_length=128)
    question_1 = models.CharField(max_length=255, blank=True, null=True)
    question_2 = models.CharField(max_length=255, blank=True, null=True)
    question_3 = models.CharField(max_length=255, blank=True, null=True)
    answer_1 = models.CharField(max_length=255, blank=True, null=True)
    answer_2 = models.CharField(max_length=255, blank=True, null=True)
    answer_3 = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'retrieve_questions'


class Students(models.Model):
    student_id = models.CharField(primary_key=True, max_length=255)
    student_name = models.CharField(max_length=128)
    gender = models.IntegerField()
    age = models.IntegerField()
    birth = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'students'


class Users(models.Model):
    gender = (
        ('male', '男'),
        ('female', '女'),
    )

    name = models.CharField(max_length=128, unique=True)
    password = models.CharField(max_length=256)
    email = models.EmailField(unique=True)
    sex = models.CharField(max_length=32, choices=gender, default='男')
    c_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['c_time']
        verbose_name = '用户'
        verbose_name_plural = '用户'

