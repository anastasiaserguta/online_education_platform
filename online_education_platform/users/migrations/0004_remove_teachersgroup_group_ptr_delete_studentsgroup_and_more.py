# Generated by Django 5.0.7 on 2024-07-27 04:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_profile_is_teacher'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='teachersgroup',
            name='group_ptr',
        ),
        migrations.DeleteModel(
            name='StudentsGroup',
        ),
        migrations.DeleteModel(
            name='TeachersGroup',
        ),
    ]
