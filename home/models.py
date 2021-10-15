from django.db import models
from django.forms import ModelForm

# Create your models here.
class Teacher(models.Model):
    first_name  = models.CharField("Họ",max_length=30)
    last_name   = models.CharField("Tên",max_length=30)
    email       = models.EmailField("Email")
    image       = models.ImageField(null=True)
    

    def __str__(self):
        return "%s %s" % (self.first_name, self.last_name)

    class Meta:
        db_table = "Teacher"

class Course(models.Model):
    headline        = models.CharField("Tiêu đề",max_length=50)
    number_students = models.CharField("Số học sinh",max_length=50, default='')
    pubday          = models.DateField("Ngày đăng")
    name_teacher    = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    content      = models.CharField("Nội dung khóa học",max_length=100,default='')
    old_price       = models.CharField("Giá cũ",max_length=25, default='')
    new_price       = models.CharField("Giá mới",max_length=25, default='')
    image           = models.ImageField(null=True)

    def __str__(self):
        return self.headline

    class Meta:
        db_table = "Course"

class Order(models.Model):
    name = models.CharField(max_length=100)
    school = models.CharField(max_length=100)
    studentclass = models.CharField(max_length=100)
    studentemail = models.CharField(max_length=100)
    phonenumber = models.CharField(max_length=100)
    course = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    class Meta:
        db_table = "Order"

class OrderForm(ModelForm):
    class Meta:
        model = Order
        fields = ['name','school','studentclass','studentemail','phonenumber','course']

class Document(models.Model):
    headline     = models.CharField("Tiêu đề",max_length=50)
    pubday       = models.DateField("Ngày đăng")
    name_teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    content      = models.TextField("Nội dung",default='')
    file = models.FileField(default='',upload_to='')

    def __str__(self):
        return self.headline

    class Meta:
        ordering = ['-id']
        db_table = "Document"

class News(models.Model):
    headline     = models.CharField("Tiêu đề",max_length=1000)
    pubday       = models.DateField("Ngày đăng")
    content      = models.TextField("Nội dung")
    link         = models.CharField("Link bài viết",max_length=150,default='')
    image        = models.ImageField(null=True)

    def __str__(self):
        return self.headline

    class Meta:
        ordering = ['-id']
        db_table = "News"

class Trainers(models.Model):
    imagetrainer = models.ImageField("Ảnh giảng viên",null=True)
    fullname = models.CharField("Họ và tên",max_length=30)
    position = models.CharField("Chuyên ngành",max_length=30)
    description = models.CharField("Mô tả",max_length=100)
    linkin4 = models.CharField("Link mạng xã hội",max_length=300,default='')

    def __str__(self):
        return self.fullname

    class Meta:
        db_table = "Trainers"
