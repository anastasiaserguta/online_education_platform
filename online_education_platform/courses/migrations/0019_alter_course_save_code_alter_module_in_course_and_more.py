# Generated by Django 5.0.7 on 2024-07-28 08:16

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0018_alter_course_save_code_alter_module_in_course_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='save_code',
            field=models.CharField(default=uuid.UUID('752f1db6-0cbc-48b8-bbe4-d4571d6178b6'), editable=False, max_length=60),
        ),
        migrations.AlterField(
            model_name='module',
            name='in_course',
            field=models.CharField(default=uuid.UUID('752f1db6-0cbc-48b8-bbe4-d4571d6178b6'), max_length=60),
        ),
        migrations.AlterField(
            model_name='module',
            name='save_code_module',
            field=models.CharField(default=uuid.UUID('443291cf-19e5-4ac7-85e3-45dfaad0235a'), editable=False, max_length=60),
        ),
        migrations.AlterField(
            model_name='solution',
            name='for_task',
            field=models.CharField(default=uuid.UUID('9a4efd69-5172-4d9e-972f-9ab6face408c'), max_length=60),
        ),
        migrations.AlterField(
            model_name='solution',
            name='solution_code',
            field=models.CharField(default='84202584221218172811829', editable=False, max_length=60, unique=True),
        ),
        migrations.AlterField(
            model_name='task',
            name='in_module',
            field=models.CharField(default=uuid.UUID('443291cf-19e5-4ac7-85e3-45dfaad0235a'), max_length=60),
        ),
        migrations.AlterField(
            model_name='task',
            name='save_code_task',
            field=models.CharField(default=uuid.UUID('9a4efd69-5172-4d9e-972f-9ab6face408c'), editable=False, max_length=60),
        ),
    ]
