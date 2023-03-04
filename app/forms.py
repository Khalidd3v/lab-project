from django import forms
from .models import *
from django.contrib.auth.models import User



class RegisterPatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = '__all__'
        widgets = {
            'doctor': forms.Select(attrs={'class': 'form-control fw-bold'}),
            'name': forms.TextInput(attrs={'class': 'form-control fw-bold', 'placeholder':'Enter Patient Name..'}),
            'gender': forms.Select(attrs={'class': 'form-control fw-bold'}),
            'address': forms.TextInput(attrs={'class': 'form-control fw-bold', 'placeholder':'Enter Patient Adress..'}),
            'age': forms.NumberInput(attrs={'class': 'form-control fw-bold'}),
            'report_date': forms.DateInput(attrs={'class': 'form-control fw-bold'}),
        }


class RegisterDoctorForm(forms.ModelForm):
    class Meta:
        model = Doctor
        fields = "__all__"
        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control fw-bold', 'placeholder':'Enter Doctor Name'}),
            'address': forms.TextInput(attrs={'class':'form-control fw-bold', 'placeholder':'Enter Doctor or Clinic Address'}),
            'phone_number': forms.TextInput(attrs={'class':'form-control fw-bold', 'placeholder':'Enter Doctor Phone Number'}),
        }