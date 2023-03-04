from django.db import models
from django.utils import timezone

class Doctor(models.Model):
    name = models.CharField(max_length=32)
    address = models.CharField( blank=True ,max_length=50)
    phone_number = models.CharField(max_length=13,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

Patient_Gender = (("male","male"), ("female","female"))


class Patient(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.DO_NOTHING)
    name = models.CharField(max_length=50)
    gender = models.CharField(choices=Patient_Gender, default="Male", max_length=10)
    age = models.IntegerField()
    report_date = models.DateTimeField(default=timezone.now)
    update_at = models.DateTimeField(auto_now=True)
    address = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    