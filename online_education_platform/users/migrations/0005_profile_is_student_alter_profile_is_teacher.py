# Generated by Django 5.0.7 on 2024-07-28 13:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_remove_teachersgroup_group_ptr_delete_studentsgroup_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='is_student',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='profile',
            name='is_teacher',
            field=models.BooleanField(default=False),
        ),
    ]
