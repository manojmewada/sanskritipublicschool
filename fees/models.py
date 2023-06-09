from django.db import models
from classform.models import ClassRoom, ClassRoomStudent
from django.core.exceptions import PermissionDenied
# Create your models here.
class Fine(models.Model):
    fine = models.IntegerField()
    student = models.ForeignKey(ClassRoomStudent, on_delete=models.CASCADE)
    category = models.CharField(max_length=100)
    submissionDate = models.DateField(null=True)
    description = models.TextField()
	

class FeeDiscount(models.Model):
	discount = models.IntegerField()
	category = models.CharField(max_length=50)
	student = models.ForeignKey(ClassRoomStudent, on_delete=models.CASCADE)
	description = models.TextField()
	total_off = models.IntegerField()


class FeeCategory(models.Model):
	once = models.BooleanField(default=True)
	submission_type = models.CharField(max_length=50)
	description = models.TextField()
	
class ClassSectionFees(models.Model):
	classSection = models.ForeignKey(ClassRoom, on_delete=models.CASCADE)
	feeCategory = models.ForeignKey(FeeCategory, on_delete=models.CASCADE)
	fees = models.IntegerField()
	def __str__(self):
	 return f"{self.classSection} {self.feeCategory} {self.fees}"

def user_directory_path(instance, filename):
    """file will be uploaded to given path"""
    return 'fee-slip/{0}/{1}'.format(instance.student.student.admissionNumber, filename)
class Fee(models.Model):
	regNo = models.IntegerField()
	classSection = models.ForeignKey(ClassRoom, on_delete=models.CASCADE)
	student = models.ForeignKey(ClassRoomStudent, on_delete=models.CASCADE)
	payment_method = models.CharField(max_length=50)
	submissionDate = models.DateField()
	amount = models.IntegerField()
	monthsPaid = models.CharField(max_length=50)
	feeSlip = models.FileField(upload_to=user_directory_path)

	def __str__(self):
	 return f"{self.student} {self.amount} {self.monthsPaid}"

class FeeCycle(models.Model):
	lastSubmissionDate = models.DateField()
	firstSubmissionDate = models.DateField()
	cycle = models.CharField(max_length=50)