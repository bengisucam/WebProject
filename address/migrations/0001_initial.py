# Generated by Django 3.0.6 on 2020-05-26 09:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country_name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city_name', models.CharField(max_length=30)),
                ('country_id', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='address.Country')),
            ],
        ),
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address_name', models.CharField(max_length=100)),
                ('zip_code', models.IntegerField(blank=True, max_length=10)),
                ('city_id', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='address.City')),
            ],
        ),
    ]
