from django import forms
from .models import *
from django.contrib.auth.models import User



#---------------------------------Doctor & Patients Forms Start Here----------------------------------------------------------------------

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







#----------------------------------------Uploud Image FORMS----------------------------------------------------------------------



class MyImageForm(forms.ModelForm):
    class Meta:
        model = MyImage
        fields = ('image', 'caption')






# #----------------------------------------Select Test Forms Starts Here----------------------------------------------------------------------



class TestSelectionForm(forms.Form):
    test_choices = (
        ('CBC Test', 'CBC Test'),
        ('Bio Chemistry Test', 'Bio Chemistry Test'),
        ('Stool RE Test', 'Stool RE Test')
    )
    tests = forms.MultipleChoiceField(choices=test_choices, widget=forms.CheckboxSelectMultiple)
    patient_id = forms.CharField(widget=forms.HiddenInput(), required=False)

#----------------------------------------All Tests Forms Starts Here----------------------------------------------------------------------

 #cbc test form       
class CBCTestForm(forms.ModelForm):
    
    class Meta:
        model = CBCTest 
        fields = '__all__'
        exclude = ['patient']

        widgets = {

            'Haemoglobin1': forms.TextInput(attrs={'class':'form-control fw-bold', 'placeholder':'Enter Value'}),
            'Total_RBC': forms.TextInput(attrs={'class':'form-control fw-bold', 'placeholder':'Enter Value'}),
            'HCT': forms.TextInput(attrs={'class':'form-control fw-bold', 'placeholder':'Enter Value'}),
            'MCV': forms.TextInput(attrs={'class':'form-control fw-bold', 'placeholder':'Enter Value'}),
            'MCH': forms.TextInput(attrs={'class':'form-control fw-bold', 'placeholder':'Enter Value'}),
            'MCHC': forms.TextInput(attrs={'class':'form-control fw-bold', 'placeholder':'Enter Value'}),
            'Total_WBC': forms.TextInput(attrs={'class':'form-control fw-bold', 'placeholder':'Enter Value'}),
            'Neutrophils': forms.TextInput(attrs={'class':'form-control fw-bold', 'placeholder':'Enter Value'}),
            'Lymphocytes': forms.TextInput(attrs={'class':'form-control fw-bold', 'placeholder':'Enter Value'}),
            'Monocytes': forms.TextInput(attrs={'class':'form-control fw-bold', 'placeholder':'Enter Value'}),
            'Eosonophils': forms.TextInput(attrs={'class':'form-control fw-bold', 'placeholder':'Enter Value'}),
            'Platelet': forms.TextInput(attrs={'class':'form-control fw-bold', 'placeholder':'Enter Value'}),
            'Basophils': forms.TextInput(attrs={'class':'form-control fw-bold', 'placeholder':'Enter Value'}),
            'ESR': forms.TextInput(attrs={'class':'form-control fw-bold', 'placeholder':'Enter Value'}),
        }

#BioChemistry Test Form

class BioChemistryTestForm(forms.ModelForm):
    class Meta:
        model = BioChemistryTest
        fields = '__all__'
        exclude = ['patient']
        widgets = {
            
            'hba1c': forms.TextInput(attrs={'class':'form-control fw-bold', 'placeholder':'Enter Value'}),
            'b_sugar_r': forms.TextInput(attrs={'class':'form-control fw-bold', 'placeholder':'Enter Value'}),
            'b_sugar_f': forms.TextInput(attrs={'class':'form-control fw-bold', 'placeholder':'Enter Value'}),
            'sgpt_alt': forms.TextInput(attrs={'class':'form-control fw-bold', 'placeholder':'Enter Value'}),
            'sgot_ast': forms.TextInput(attrs={'class':'form-control fw-bold', 'placeholder':'Enter Value'}),
            'alk_phosphatase': forms.TextInput(attrs={'class':'form-control fw-bold', 'placeholder':'Enter Value'}),
            'sbillirubin_total': forms.TextInput(attrs={'class':'form-control fw-bold', 'placeholder':'Enter Value'}),
            'sbillirubin_direct': forms.TextInput(attrs={'class':'form-control fw-bold', 'placeholder':'Enter Value'}),
            'sbillirubin_indirect': forms.TextInput(attrs={'class':'form-control fw-bold', 'placeholder':'Enter Value'}),
            's_calium': forms.TextInput(attrs={'class':'form-control fw-bold', 'placeholder':'Enter Value'}),
            's_uric_acid': forms.TextInput(attrs={'class':'form-control fw-bold', 'placeholder':'Enter Value'}),
            'b_urea': forms.TextInput(attrs={'class':'form-control fw-bold', 'placeholder':'Enter Value'}),
            's_creatinine': forms.TextInput(attrs={'class':'form-control fw-bold', 'placeholder':'Enter Value'}),
            's_amylase': forms.TextInput(attrs={'class':'form-control fw-bold', 'placeholder':'Enter Value'}),
            's_cholestrol': forms.TextInput(attrs={'class':'form-control fw-bold', 'placeholder':'Enter Value'}),
            'triglycerides': forms.TextInput(attrs={'class':'form-control fw-bold', 'placeholder':'Enter Value'}),
            'hdl': forms.TextInput(attrs={'class':'form-control fw-bold', 'placeholder':'Enter Value'}),
            'ldl': forms.TextInput(attrs={'class':'form-control fw-bold', 'placeholder':'Enter Value'}),
            'ldh': forms.TextInput(attrs={'class':'form-control fw-bold', 'placeholder':'Enter Value'}),
            't_protien': forms.TextInput(attrs={'class':'form-control fw-bold', 'placeholder':'Enter Value'}),
            'cpk': forms.TextInput(attrs={'class':'form-control fw-bold', 'placeholder':'Enter Value'}),
            'crp': forms.TextInput(attrs={'class':'form-control fw-bold', 'placeholder':'Enter Value'}),
        }

# Stool R/E Test Form

class StoolRETestForm(forms.ModelForm):
    class Meta:
        model = StoolRETest
        fields = '__all__'
        exclude = ['patient']
        widgets = {

            
            'color': forms.TextInput(attrs={'class':'form-control fw-bold', 'placeholder':'Enter Value'}),
            'mucus': forms.TextInput(attrs={'class':'form-control fw-bold', 'placeholder':'Enter Value'}),
            'ova': forms.TextInput(attrs={'class':'form-control fw-bold', 'placeholder':'Enter Value'}),
            'cyst': forms.TextInput(attrs={'class':'form-control fw-bold', 'placeholder':'Enter Value'}),
            'puss_cells': forms.TextInput(attrs={'class':'form-control fw-bold', 'placeholder':'Enter Value'}),
            'rbcs': forms.TextInput(attrs={'class':'form-control fw-bold', 'placeholder':'Enter Value'}),
            'backteria': forms.TextInput(attrs={'class':'form-control fw-bold', 'placeholder':'Enter Value'}),
            'stool_hpylori': forms.TextInput(attrs={'class':'form-control fw-bold', 'placeholder':'Enter Value'}),


        }








