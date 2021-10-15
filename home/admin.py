from django.contrib import admin
from .models import Document, News, Order, Teacher, Course, Trainers

# Register your models here.
admin.site.register(Teacher)
admin.site.register(Course)
admin.site.register(Document)
admin.site.register(News)
admin.site.register(Trainers)
admin.site.register(Order)
