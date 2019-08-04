from django.shortcuts import render, redirect
from . import models
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .forms import UserForm, RegisterForm, ForgetForm, ResetForm, RetrieveForm, GradeForm
import hashlib

# Create your views here.


def index(request):
    pass
    return render(request, 'login/index.html')


def login(request):
    if request.session.get('is_login', None):
        return redirect('/index/')
    if request.method == "POST":
        login_form = UserForm(request.POST)
        message = "请检查填写的内容！"
        if login_form.is_valid():
            username = login_form.cleaned_data['username']
            password = login_form.cleaned_data['password']
            obj = hashlib.md5(password.encode("utf-8"))
            hl = obj.hexdigest()
            hl_new = hashlib.md5(hl.encode("utf-8"))
            password = hl_new.hexdigest() + 'HELLO'
            try:
                user = models.User.objects.get(name=username)
                if user.password == password:
                    request.session['is_login'] = True
                    request.session['user_id'] = user.id
                    request.session['user_name'] = user.name
                    request.session['c_kind'] = user.c_kind
                    return redirect('/index/')
                else:
                    message = "密码不正确！"
            except:
                message = "用户不存在！"
        return render(request, 'login/login.html', locals())

    login_form = UserForm()
    return render(request, 'login/login.html', locals())


def register(request):
    if request.session.get('is_login', None):  # 登录状态不允许注册。
        return redirect("/index/")
    if request.method == "POST":
        register_form = RegisterForm(request.POST)
        message = "请检查填写的内容！"
        if register_form.is_valid():  # 获取数据
            username = register_form.cleaned_data['username']
            password1 = register_form.cleaned_data['password1']
            password2 = register_form.cleaned_data['password2']
            email = register_form.cleaned_data['email']
            sex = register_form.cleaned_data['sex']
            question_1 = register_form.cleaned_data['question_1']
            question_2 = register_form.cleaned_data['question_2']
            question_3 = register_form.cleaned_data['question_3']
            answer_1 = register_form.cleaned_data['answer_1']
            answer_2 = register_form.cleaned_data['answer_2']
            answer_3 = register_form.cleaned_data['answer_3']
            if password1 != password2:  # 判断两次密码是否相同
                message = "两次输入的密码不同！"
                return render(request, 'login/register.html', locals())
            else:
                same_name_user = models.User.objects.filter(name=username)
                if same_name_user:  # 用户名唯一
                    message = '用户已经存在，请重新选择用户名！'
                    return render(request, 'login/register.html', locals())
                same_email_user = models.User.objects.filter(email=email)
                if same_email_user:  # 邮箱地址唯一
                    message = '该邮箱地址已被注册，请使用别的邮箱！'
                    return render(request, 'login/register.html', locals())  # 当一切都OK的情况下，创建新用户
                new_retrieve = models.RetrieveQuestion.objects.create()
                new_retrieve.name = username
                new_retrieve.question_1 = question_1
                new_retrieve.question_2 = question_2
                new_retrieve.question_3 = question_3
                new_retrieve.answer_1 = answer_1
                new_retrieve.answer_2 = answer_2
                new_retrieve.answer_3 = answer_3
                new_retrieve.save()

                obj = hashlib.md5(password1.encode("utf-8"))
                hl = obj.hexdigest()
                hl_new = hashlib.md5(hl.encode("utf-8"))

                new_user = models.User.objects.create()
                new_user.name = username
                new_user.password = hl_new.hexdigest() + 'HELLO'
                new_user.email = email
                new_user.sex = sex
                new_user.save()
                return redirect('/login/')  # 自动跳转到登录页面
    register_form = RegisterForm()
    return render(request, 'login/register.html', locals())


def logout(request):
    if not request.session.get('is_login', None):
        return redirect("/index/")
    request.session.flush()
    return redirect("/index/")


def user_info(request):
    all_user = models.User.objects.all()
    return render(request, 'login/userinfo.html', locals())


def class_info(request):
    all_student = models.Student.objects.all()
    all_grade = models.Grade.objects.all()
    return render(request, 'login/classinfo.html', locals())


def grade_info(request, student_id):
    exact_student = models.Student.objects.get(student_id=student_id)
    exact_grade = models.Grade.objects.filter(student_id=student_id)
    return render(request, 'login/gradeinfo.html', locals())


@csrf_exempt  # 局部禁用csrf
def grade_update(request):
    # print("==>", request.POST.get('pk'), request.POST.get('value'))
    if request.method == "POST":
        pk_list = request.POST.get('pk').split(',')
        new_grade = request.POST.get('value')
        ret = models.Grade.objects.get(student_id=pk_list[0], class_id=pk_list[1])
        ret.grade = new_grade
        ret.grade_point = set_grade_point(new_grade)
        ret.save()
    return HttpResponse('ok')


def grade_add(request):
    if request.method == "POST":
        grade_form = GradeForm(request.POST)
        message = "请检查填写的内容！"
        if grade_form.is_valid():
            student_id = request.GET.get('student_id')
            new_grade_record = models.Grade.objects.create(student_id=student_id, class_id=0, class_name=0, grade=0)
            new_grade_record.student_id = student_id
            new_grade_record.class_id = grade_form.cleaned_data['new_class_id']
            new_grade_record.class_name = grade_form.cleaned_data['new_class_name']
            new_grade_record.grade = str(grade_form.cleaned_data['new_grade'])
            new_grade_record.grade_point = set_grade_point(new_grade_record.grade)

            exist_class_id = models.Grade.objects.filter(class_id=new_grade_record.class_id)
            exist_class_name = models.Grade.objects.filter(class_name=new_grade_record.class_name)
            if exist_class_id or exist_class_name:
                message = "该课程已存在，请直接修改成绩！"
                return render(request, 'login/gradeadd.html', locals())

            new_grade_record.save()
            return redirect('/classinfo/')
    grade_form = GradeForm()
    return render(request, 'login/gradeadd.html', locals())


@csrf_exempt
def grade_delete(request):
    if request.method == "POST":
        check_box_list = request.POST.getlist('check_box_list')
        for delete_unit in check_box_list:
            models.Grade.objects.filter(class_id=delete_unit).delete()
        return redirect('/classinfo/')
    return redirect(request)


def forget(request):
    if request.method == "POST":
        forget_form = ForgetForm(request.POST)
        message = "请检查填写的内容！"
        if forget_form.is_valid():
            email = forget_form.cleaned_data['email']
            global email_address
            email_address = forget_form.cleaned_data['email']
            email_exist = models.User.objects.filter(email=email)
            if not email_exist:
                message = "该邮箱未注册！"
                return render(request, 'login/forget.html', locals())
            else:
                return redirect('/forget/retrieve/')
    forget_form = ForgetForm()
    return render(request, 'login/forget.html', locals())


def retrieve(request):
    ret = models.User.objects.get(email=email_address)
    q_and_a = models.RetrieveQuestion.objects.get(name=ret.name)
    if request.method == "POST":
        retrieve_form = RetrieveForm(request.POST)
        message = "请检查填写的内容！"
        if retrieve_form.is_valid():
            answer_1 = retrieve_form.cleaned_data['answer_1']
            answer_2 = retrieve_form.cleaned_data['answer_2']
            answer_3 = retrieve_form.cleaned_data['answer_3']
            correct_answer_1 = q_and_a.answer_1
            correct_answer_2 = q_and_a.answer_2
            correct_answer_3 = q_and_a.answer_3
            if answer_1 != correct_answer_1 or answer_2 != correct_answer_2 or answer_3 != correct_answer_3:
                message = "密保问题答案不正确！"
                return render(request, 'login/retrieve.html', locals())
            else:
                return redirect('/forget/resetpwd/')
    retrieve_form = RetrieveForm()
    return render(request, 'login/retrieve.html', locals())


def resetpwd(request):
    if request.method == "POST":
        reset_form = ResetForm(request.POST)
        message = "请检查填写的内容！"
        if reset_form.is_valid():
            new_password_1 = reset_form.cleaned_data['new_password1']
            new_password_2 = reset_form.cleaned_data['new_password2']
            if new_password_1 != new_password_2:
                message = "两次输入的密码不同！"
                return render(request, 'login/reset.html', locals())
            else:
                modify_user = models.User.objects.get(email=email_address)
                obj = hashlib.md5(new_password_1.encode("utf-8"))
                hl = obj.hexdigest()
                hl_new = hashlib.md5(hl.encode("utf-8"))
                modify_user.password = hl_new.hexdigest()+'HELLO'
                modify_user.save()
                return redirect('/login/')
    reset_form = ResetForm()
    return render(request, 'login/reset.html', locals())


def set_grade_point(new_grade):
    grade = int(new_grade)
    if grade >= 90:
        grade_point = 4.0
    elif grade >= 85:
        grade_point = 3.7
    elif grade >= 82:
        grade_point = 3.3
    elif grade >= 78:
        grade_point = 3.0
    elif grade >= 75:
        grade_point = 2.7
    elif grade >= 72:
        grade_point = 2.3
    elif grade >= 68:
        grade_point = 2.0
    elif grade >= 64:
        grade_point = 1.5
    elif grade >= 60:
        grade_point = 1.3
    else:
        grade_point = 0.0

    return grade_point
