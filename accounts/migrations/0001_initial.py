# Generated by Django 3.0.3 on 2020-05-16 21:46

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('user_id', models.UUIDField(default=uuid.UUID('26841884-fccb-470b-a1e7-5c413f4d7677'), editable=False, primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('gender', models.CharField(choices=[('FEMALE', 'female'), ('MALE', 'male')], max_length=6)),
                ('is_active', models.BooleanField()),
            ],
            options={
                'abstract': False,
            },
        ),
    ]