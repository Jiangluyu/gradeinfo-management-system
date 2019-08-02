from django import forms
from captcha.fields import CaptchaField


class UserForm(forms.Form):
    username = forms.CharField(label="用户名", max_length=128, widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label="密码", max_length=256, widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    captcha = CaptchaField(label="验证码")


class RegisterForm(forms.Form):
    gender = (
        ('male', "男"),
        ('female', "女"),
    )
    username = forms.CharField(label="用户名", max_length=128, widget=forms.TextInput(attrs={'class': 'form-control'}))
    password1 = forms.CharField(label="密码", max_length=256, widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(label="确认密码", max_length=256,
                                widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(label="邮箱地址", widget=forms.EmailInput(attrs={'class': 'form-control'}))
    sex = forms.ChoiceField(label="性别", choices=gender)
    captcha = CaptchaField(label="验证码")
    question_1 = forms.CharField(label="密保问题01", max_length=255,
                                 widget=forms.TextInput(attrs={'class': 'form-control'}))
    answer_1 = forms.CharField(label="问题答案01", max_length=255, widget=forms.TextInput(attrs={'class': 'form-control'}))
    question_2 = forms.CharField(label="密保问题02", max_length=255,
                                 widget=forms.TextInput(attrs={'class': 'form-control'}))
    answer_2 = forms.CharField(label="问题答案02", max_length=255, widget=forms.TextInput(attrs={'class': 'form-control'}))
    question_3 = forms.CharField(label="密保问题03", max_length=255,
                                 widget=forms.TextInput(attrs={'class': 'form-control'}))
    answer_3 = forms.CharField(label="问题答案03", max_length=255, widget=forms.TextInput(attrs={'class': 'form-control'}))


class ForgetForm(forms.Form):
    email = forms.EmailField(label="邮箱", widget=forms.EmailInput(attrs={'class': 'form-control'}))
    captcha = CaptchaField(label="验证码")


class RetrieveForm(forms.Form):
    answer_1 = forms.CharField(label="问题答案01", max_length=255, widget=forms.TextInput(attrs={'class': 'form-control'}))
    answer_2 = forms.CharField(label="问题答案02", max_length=255, widget=forms.TextInput(attrs={'class': 'form-control'}))
    answer_3 = forms.CharField(label="问题答案03", max_length=255, widget=forms.TextInput(attrs={'class': 'form-control'}))


class ResetForm(forms.Form):
    new_password1 = forms.CharField(label="请输入新密码", required=True, min_length=6,
                                    error_messages={'required': '密码不能为空.', 'min_length': "至少6位"},
                                    widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    new_password2 = forms.CharField(label="再次输入新密码", required=True, min_length=6,
                                    error_messages={'required': '密码不能为空.', 'min_length': "至少6位"},
                                    widget=forms.PasswordInput(attrs={'class': 'form-control'}))


class GradeForm(forms.Form):
    new_class_id = forms.CharField(label="课程号", required=True, error_messages={'required': '课程号不能为空！'},
                                   widget=forms.TextInput(attrs={'class': 'form-control'}))
    new_class_name = forms.CharField(label="课程名", required=True, error_messages={'required': '课程名不能为空！'},
                                     widget=forms.TextInput(attrs={'class': 'form-control'}))
    new_grade = forms.CharField(label="成绩", required=True, error_messages={'required': '成绩不能为空！'},
                                widget=forms.TextInput(attrs={'class': 'form-control'}))

