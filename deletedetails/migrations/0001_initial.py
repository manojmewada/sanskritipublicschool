# Generated by Django 4.1.7 on 2023-03-20 08:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DeletedEmployee',
            fields=[
                ('empID', models.IntegerField(default=0, primary_key=True, serialize=False)),
                ('firstName', models.CharField(blank=True, max_length=20)),
                ('lastName', models.CharField(blank=True, max_length=20)),
                ('fullName', models.CharField(blank=True, max_length=50)),
                ('father_name', models.CharField(blank=True, max_length=50)),
                ('mother_name', models.CharField(blank=True, max_length=50)),
                ('partnerName', models.CharField(blank=True, max_length=50)),
                ('gender', models.CharField(blank=True, max_length=20)),
                ('email', models.CharField(blank=True, max_length=40)),
                ('dob', models.DateField(blank=True, null=True)),
                ('joiningDate', models.DateField(blank=True, null=True)),
                ('bloodGroup', models.CharField(blank=True, max_length=20)),
                ('mobile_number', models.BigIntegerField(default=0)),
                ('marital_status', models.CharField(blank=True, max_length=20)),
                ('experience', models.CharField(blank=True, max_length=20)),
                ('aadharNumber', models.BigIntegerField(default=0)),
                ('empCategory', models.CharField(blank=True, max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='DeletedStudentInfo',
            fields=[
                ('firstName', models.CharField(blank=True, max_length=20)),
                ('lastName', models.CharField(blank=True, max_length=20)),
                ('fullName', models.CharField(blank=True, max_length=50)),
                ('gender', models.CharField(blank=True, max_length=20)),
                ('dob', models.DateField(blank=True, null=True)),
                ('classSection', models.CharField(blank=True, max_length=20)),
                ('admissionNumber', models.BigIntegerField(primary_key=True, serialize=False)),
                ('mobileNumber', models.BigIntegerField(blank=True, null=True)),
                ('religion', models.CharField(blank=True, max_length=20)),
                ('caste', models.CharField(blank=True, max_length=20)),
                ('tcNumber', models.BigIntegerField(blank=True, null=True)),
                ('aadharNumber', models.BigIntegerField(blank=True, null=True)),
                ('feeWaiverCategory', models.CharField(blank=True, max_length=20)),
                ('prevSchoolName', models.CharField(blank=True, max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='DeletedCurrentAddress',
            fields=[
                ('student', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='deletedetails.deletedstudentinfo')),
                ('Address', models.CharField(blank=True, max_length=100)),
                ('Address1', models.CharField(blank=True, max_length=100)),
                ('Address2', models.CharField(blank=True, max_length=100)),
                ('zipCode', models.BigIntegerField(blank=True, null=True)),
                ('state', models.CharField(blank=True, max_length=20)),
                ('city', models.CharField(blank=True, max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='DeletedEmployeeCurrentAddress',
            fields=[
                ('employee', models.OneToOneField(blank=True, on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='deletedetails.deletedemployee')),
                ('Address', models.CharField(blank=True, max_length=100)),
                ('Address1', models.CharField(blank=True, max_length=100)),
                ('Address2', models.CharField(blank=True, max_length=100)),
                ('zipCode', models.BigIntegerField(default=0)),
                ('state', models.CharField(blank=True, max_length=20)),
                ('city', models.CharField(blank=True, max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='DeletedEmployeePermanentAddress',
            fields=[
                ('employee', models.OneToOneField(blank=True, on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='deletedetails.deletedemployee')),
                ('Address', models.CharField(blank=True, max_length=100)),
                ('Address1', models.CharField(blank=True, max_length=100)),
                ('Address2', models.CharField(blank=True, max_length=100)),
                ('zipCode', models.BigIntegerField(default=0)),
                ('state', models.CharField(blank=True, max_length=20)),
                ('city', models.CharField(blank=True, max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='DeletedParentInfo',
            fields=[
                ('student', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='parent', serialize=False, to='deletedetails.deletedstudentinfo')),
                ('fatherName', models.CharField(blank=True, max_length=20)),
                ('motherName', models.CharField(blank=True, max_length=20)),
                ('Fatherdob', models.DateField(blank=True, null=True)),
                ('Motherdob', models.DateField(blank=True, null=True)),
                ('MobileNumber', models.BigIntegerField(blank=True, null=True)),
                ('altMobileNumber', models.BigIntegerField(blank=True, null=True)),
                ('gaurdianQual', models.CharField(blank=True, max_length=30)),
                ('guardianOccup', models.CharField(blank=True, max_length=20)),
                ('email', models.CharField(blank=True, max_length=30)),
                ('motherQual', models.CharField(blank=True, max_length=30)),
                ('motherOccup', models.CharField(blank=True, max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='DeletedPermanentAddress',
            fields=[
                ('student', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='deletedetails.deletedstudentinfo')),
                ('Address', models.CharField(blank=True, max_length=100)),
                ('Address1', models.CharField(blank=True, max_length=100)),
                ('Address2', models.CharField(blank=True, max_length=100)),
                ('zipCode', models.BigIntegerField(blank=True, null=True)),
                ('state', models.CharField(blank=True, max_length=20)),
                ('city', models.CharField(blank=True, max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='DeletedTeacher',
            fields=[
                ('employee', models.OneToOneField(blank=True, on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='deletedetails.deletedemployee')),
                ('specialization', models.CharField(blank=True, max_length=50)),
                ('designation', models.CharField(blank=True, max_length=50)),
                ('classTeacher', models.CharField(blank=True, max_length=50)),
            ],
        ),
    ]