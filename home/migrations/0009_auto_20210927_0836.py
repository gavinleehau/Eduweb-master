# Generated by Django 3.2.7 on 2021-09-27 01:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_auto_20210926_1525'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='image',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='news',
            name='content',
            field=models.CharField(max_length=150, verbose_name='Nội dung'),
        ),
    ]
