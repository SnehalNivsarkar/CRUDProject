# Generated by Django 3.1 on 2020-12-04 09:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EmployeeModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('eno', models.IntegerField()),
                ('ename', models.CharField(max_length=20)),
                ('esal', models.IntegerField()),
                ('ecity', models.CharField(max_length=20)),
            ],
        ),
    ]