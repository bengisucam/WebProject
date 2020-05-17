# Generated by Django 3.0.3 on 2020-05-17 19:23

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_auto_20200517_1148'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='user_id',
            field=models.UUIDField(default=uuid.UUID('6a957ab1-9fe5-4168-9af3-283f38933e70'), editable=False, primary_key=True, serialize=False),
        ),
    ]