# Generated by Django 4.1.7 on 2023-03-20 08:00

from django.db import migrations, models
import visitors.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Visitor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('mobile_no', models.BigIntegerField()),
                ('date_time', models.DateTimeField()),
                ('contact_to', models.CharField(max_length=30)),
                ('address', models.CharField(max_length=50)),
                ('purpose', models.TextField(max_length=30)),
                ('photo', models.FileField(upload_to=visitors.models.user_directory_path)),
                ('document', models.FileField(upload_to=visitors.models.user_directory_path)),
            ],
        ),
    ]
