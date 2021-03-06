# Generated by Django 2.0.7 on 2018-07-18 23:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('FirstName', models.CharField(blank=True, default='', max_length=100)),
                ('MiddleInitial', models.CharField(blank=True, default='', max_length=100)),
                ('LastName', models.CharField(blank=True, default='', max_length=100)),
                ('DateOfBirth', models.DateField(blank=True)),
                ('DateOfEmployment', models.DateField(blank=True)),
                ('Status', models.BooleanField(default=False)),
            ],
        ),
    ]
