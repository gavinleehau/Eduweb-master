# Generated by Django 3.2.7 on 2021-09-29 08:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0017_auto_20210929_1036'),
    ]

    operations = [
        migrations.AddField(
            model_name='document',
            name='content_detail',
            field=models.TextField(default='', verbose_name='Nội dung chính'),
        ),
    ]
