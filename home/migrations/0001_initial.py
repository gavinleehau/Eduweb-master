# Generated by Django 3.2.7 on 2021-09-25 13:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30, verbose_name='Họ')),
                ('last_name', models.CharField(max_length=30, verbose_name='Tên')),
                ('email', models.EmailField(max_length=254, verbose_name='Email')),
            ],
            options={
                'db_table': 'Teacher',
            },
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('headline', models.CharField(max_length=50)),
                ('name_teacher', models.CharField(max_length=30)),
                ('pubday', models.DateField()),
                ('price', models.CharField(max_length=30)),
                ('teacher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.teacher')),
            ],
            options={
                'db_table': 'Course',
            },
        ),
    ]
