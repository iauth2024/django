# Generated by Django 5.0.2 on 2024-02-24 06:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('kifalat', '0002_rename_class_name_student_class_field_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='progress',
            old_name='submission_date',
            new_name='paid_date',
        ),
    ]
