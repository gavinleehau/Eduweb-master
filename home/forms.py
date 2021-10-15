from django.forms import ModelForm, fields, Form
from django import forms
from django.core.exceptions import ValidationError
from .models import News, Teacher, Course, Document
from django.contrib.auth.models import User

# class TeacherForm(ModelForm):
#     class Meta:
#         model  = Teacher
#         fields = "__all__"


# class CourseForm(ModelForm):
#     class Meta:
#         model  = Course
#         fields = "__all__"



# class DocumentForm(ModelForm):
#     class Meta:
#         model  = Document
#         fields = "__all__"


# class NewsForm(ModelForm):
#     class Meta:
#         model  = News
#         fields = "__all__"


# user_views
class RegisterForm(Form):
    username     =forms.CharField(label="Tên Đăng Nhập", widget=forms.TextInput(attrs={"class": "form-control", "id": "user"}))
    password     = forms.CharField(label="Mật Khẩu", widget=forms.PasswordInput(attrs={"class": "form-control", "id": "pass"}))
    confirm_pass = forms.CharField(label="Nhập Lại Mật Khẩu", widget=forms.PasswordInput(attrs={"class": "form-control", "id": "cfpass"}))
    first_name   = forms.CharField(label="Họ", widget=forms.TextInput(attrs={"class": "form-control", "id": "firstname"}))
    last_name    = forms.CharField(label="Tên", widget=forms.TextInput(attrs={"class": "form-control", "id": "lastname"}))
    email        = forms.EmailField(label="Nhập emai", widget=forms.EmailInput(attrs={"class": "form-control", "id": "emai"}))

    def clean_username(self):
        input_username = self.cleaned_data['username']
        try:
            User.objects.get(username=input_username)
            raise ValidationError(f"Tên đăng nhập {input_username} đã tồn tại. Vui lòng nhập tên khác")
        except User.DoesNotExist:
            return input_username

    def clean_email(self):
        input_email = self.cleaned_data['email']
        try:
            User.objects.get(email=input_email)
            raise ValidationError(f"Email {input_email} đã tồn tại. Vui lòng nhập email khác")
        except User.DoesNotExist:
            return input_email
    
    def clean_confirm_pass(self):
        input_password     = self.cleaned_data['password']
        input_confirm_pass = self.cleaned_data['confirm_pass']
        if input_password != input_confirm_pass: # làm thêm về độ mạnh mật khẩu
            raise ValidationError(f"Mật khẩu không trùng nhau")
        return 

    def save_user(self):
        User.objects.create_user(
            username=self.cleaned_data['username'],
            password=self.cleaned_data['password'],
            email=self.cleaned_data['email'],
            first_name=self.cleaned_data['first_name'],
            last_name=self.cleaned_data['last_name'],
        )


class LoginForm(Form):
    username = forms.CharField(label="Tên Đăng Nhập", widget=forms.TextInput(attrs={"class": "form-control", "id": "user"}))
    password = forms.CharField(label="Mật Khẩu", widget=forms.PasswordInput(attrs={"class": "form-control", "id": "pass"}))