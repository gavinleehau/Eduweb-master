from django.shortcuts import render
from django.http import HttpResponse, response
from home.models import News, Order, Teacher, Course, Document, Trainers, OrderForm
# from .forms import TeacherForm, CourseForm
from django.views.generic import ListView, DeleteView
from django.views.generic.edit import CreateView, UpdateView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages

# Create your views here.

def index(request):
    # response = HttpResponse()
    # response.write("<h1> skfefj </h1>")
    news = News.objects.all().order_by('-id')[0:3]
    documents = Document.objects.all().order_by('-id')[0:4]
    courses = Course.objects.all().order_by('-id')[0:3]
    teachers = Teacher.objects.all()

    return render(
        request=request,
        template_name="index.html",
        context={
            'courses': courses,
            'news': news,
            'documents':documents,
            'teachers':teachers,
        }
    )

def Courses(request):
    courses   = Course.objects.all()
    teachers = Teacher.objects.all()
    return render(
        request=request,
        template_name="courses.html",
        context={
            'courses': courses,
            'teachers':teachers,
        }
    )

def About(request):
    return render(
        request=request,
        template_name="about.html",
        context={}
    )
def Contact(request):
    return render(
        request=request,
        template_name="contact.html",
        context={}
    )
def New(request):
    news = News.objects.all()
    return render(
        request=request,
        template_name="news.html",
        context={
            'news':news,
        }
    )
def NewDetail(request, news_id):
    news_detail = News.objects.get(id = news_id)
    return render(
        request=request,
        template_name="news-detail.html",
        context={
            'news_detail': news_detail,
        }
    )

@login_required(login_url="/login")
def Documents(request):
    documents   = Document.objects.all()
    return render(
        request=request,
        template_name="documents.html",
        context={
            'documents': documents,
        }
    )

@login_required(login_url="/login")
def DocumentDetail(request,document_id):
    document_detail   = Document.objects.get(id = document_id)
    return render(
        request= request ,
        template_name= "document_detail.html",
        context={
            'document_detail': document_detail ,
        }
    )

def RegisterCourse(request,course_id):
    courses_in4   = Course.objects.get(id = course_id)
    return render(
        request=request,
        template_name= "signup-course.html",
        context={
            'courses_in4': courses_in4 ,
        }
    )
   

# course
# C
class CreateCourse(CreateView):
    model = Course
    fields = "__all__"
    template_name = "course/add_course.html"


def RegisterCourse(request,course_id):
    courses_in4   = Course.objects.get(id = course_id)
    if request.method == 'POST':
        # form = OrderForm(request.POST)
        # name=request.POST['name']
        # school=request.POST['school']
        # studentclass=request.POST['studentclass']
        # studentemail=request.POST['studentemail']
        # phonebumber=request.POST['phonebumber']
        # course=request.POST['course']

        # print(name)
        data = Order()
        data.name =request.POST['name']
        data.school = request.POST['school']
        data.studentclass = request.POST['studentclass']
        data.studentemail = request.POST['studentemail']
        data.phonenumber = request.POST['phonenumber']
        data.course = courses_in4
        data.save()
        subject = "tiêu đề "
        mess = "Gửi bạn " + data.name +" "  + "\n\nĐã đăng kí thàng công!!!"
        send_mail(subject, mess, settings.EMAIL_HOST_USER, [data.studentemail,'info@ngocanh.edu.vn'])
        messages.success(request, "Khóa học của bạn đã được đăng ký thành công. Xin cảm ơn đã tin tưởng và học tập tại cơ sở của chúng tôi ! ")
        return render(
            request=request,
            template_name= "signup-course.html",
            context={
                'courses_in4': courses_in4 ,
            }
        )
    return render(
        request=request,
        template_name= "signup-course.html",
        context={
            'courses_in4': courses_in4 ,
        }
    ) 




# # R
# class ListCourse(ListView):
#     model = Course
#     template_name = "index.html"

# # U
# class UpdateCourse(UpdateView):
#     model = Course
#     fields = "__all__"
#     template_name = "course/update_course.html"

# # D
# class DeleteCourse(DeleteView):
#     model = Course
#     # fields = "__all__"
#     template_name = "course/delete_course.html"


# #teacher
# class CreateTeacher(CreateView):
#     model = Teacher
#     fields = "__all__"
#     template_name = "teacher/add_teacher.html"

# class ListTeacher(ListView):
#     model = Teacher
#     template_name = "index.html"

# class UpdateTeacher(UpdateView):
#     model = Teacher
#     fields = "__all__"
#     template_name = "teacher/update_teacher.html"

# class DeleteTeacher(DeleteView):
#     model = Teacher
#     template_name = "teacher/delete_teacher.html"


# # Document
# class CreateDocument(CreateView):
#     model = Document
#     fields        = "__all__"
#     template_name = "document/add_doc.html"

# @method_decorator(login_required(login_url="/login"),name="dispatch")
# class ListDocument(ListView):
#     model = Document
#     template_name = "index.html"


# # @method_decorator(login_required(login_url="/login"),name="dispatch")


# @method_decorator(login_required(login_url="/login"),name="dispatch")
# class UpdateDocument(UpdateView):
#     model = Document
#     fields        = "__all__"
#     template_name = "document/update_document.html"

# @method_decorator(login_required(login_url="/login"),name="dispatch")
# class DeleteDocument(DeleteView):
#     model = Document
#     template_name = "document/delete_document.html"


# # News
# class CreateNews(CreateView):
#     model = News
#     fields        = "__all__"
#     template_name = "news/add_news.html"

# class ListNews(ListView):
#     model = News
#     template_name = "index.html"

# class UpdateNews(UpdateView):
#     model = News
#     fields        = "__all__"
#     template_name = "news/update_document.html"

# class DeleteNews(DeleteView):
#     model = News
#     template_name = "news/news.html"


