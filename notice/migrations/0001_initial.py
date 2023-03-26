# Generated by Django 4.1.7 on 2023-03-20 08:00

from django.db import migrations, models
import django.db.models.deletion
import notice.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('classform', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='StudentNotice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('notice', models.TextField()),
                ('notice_document', models.FileField(blank=True, upload_to=notice.models.student_directory_path)),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='classform.classroomstudent')),
            ],
        ),
        migrations.CreateModel(
            name='ClassNotice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('notice', models.TextField()),
                ('notice_document', models.FileField(blank=True, upload_to=notice.models.user_directory_path)),
                ('classRoom', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='classform.classroom')),
            ],
        ),
    ]
