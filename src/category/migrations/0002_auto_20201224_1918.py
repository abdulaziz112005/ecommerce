# Generated by Django 3.1.4 on 2020-12-24 14:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='brend',
            name='logo',
            field=models.ImageField(max_length=200, upload_to='brends'),
        ),
        migrations.AlterField(
            model_name='category',
            name='photo',
            field=models.ImageField(max_length=200, upload_to='categories'),
        ),
    ]
