# Generated by Django 4.2.1 on 2023-05-20 20:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todo_api', '0002_alter_task_status'),
    ]

    operations = [
        migrations.RenameField(
            model_name='task',
            old_name='status',
            new_name='completed',
        ),
    ]
