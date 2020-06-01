# Generated by Django 3.0.6 on 2020-05-28 14:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('date_of_birth', models.DateField(blank=True)),
                ('gender', models.CharField(choices=[('FEMALE', 'Female'), ('MALE', 'Male')], max_length=6)),
                ('email', models.EmailField(max_length=100)),
                ('password', models.CharField(max_length=30)),
                ('is_active', models.BooleanField(max_length=10)),
                ('role', models.CharField(choices=[('MANAGER', 'Manager'), ('INSTRUCTOR', 'Instructor'), ('CUSTOMER', 'Customer')], default='Instructor', max_length=10)),
            ],
        ),
    ]
