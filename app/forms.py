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







#----------------------------------------Select Test CHECKBOX FORMS----------------------------------------------------------------------



# class SelectTestForm(forms.Form):
    
#     CBCTest = forms.BooleanField(label='CBCTest', required=False)
#     BioChemistryTest = forms.BooleanField(label='BioChemistryTest', required=False)
#     StoolRETest = forms.BooleanField(label='StoolRETest', required=False)






# #----------------------------------------All Tests Forms Starts Here----------------------------------------------------------------------



class TestSelectionForm(forms.Form):
    test_choices = (
        ('CBC Test', 'CBC Test'),
        ('Bio Chemistry Test', 'Bio Chemistry Test'),
        ('Stool RE Test', 'Stool RE Test')
    )
    tests = forms.MultipleChoiceField(choices=test_choices, widget=forms.CheckboxSelectMultiple)
    patient_id = forms.CharField(widget=forms.HiddenInput(), required=False)
# #----------------------------------------All Tests Forms Starts Here----------------------------------------------------------------------

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





class MyImageForm(forms.ModelForm):
    class Meta:
        model = MyImage
        fields = ('image', 'caption')


# class AddTestForm(forms.ModelForm):
#     class Meta:
#         model = Tests
#         fields = '__all__'
#         exclude = ['patient']
#         widgets = {

#             'label_1': forms.TextInput(attrs={'class':'form-control fw-bold', 'placeholder':'Enter Name of Test Attribute'}),
#             'value_1': forms.TextInput(attrs={'class':'form-control fw-bold', 'placeholder':'Enter Value of Test Attribute'}),

#             'label_2': forms.TextInput(attrs={'class':'form-control fw-bold', 'placeholder':'Enter Name of Test Attribute'}),
#             'value_2': forms.TextInput(attrs={'class':'form-control fw-bold', 'placeholder':'Enter Value of Test Attribute'}),

#             'label_3': forms.TextInput(attrs={'class':'form-control fw-bold', 'placeholder':'Enter Name of Test Attribute'}),
#             'value_3': forms.TextInput(attrs={'class':'form-control fw-bold', 'placeholder':'Enter Value of Test Attribute'}),

#             'label_4': forms.TextInput(attrs={'class':'form-control fw-bold', 'placeholder':'Enter Name of Test Attribute'}),
#             'value_4': forms.TextInput(attrs={'class':'form-control fw-bold', 'placeholder':'Enter Value of Test Attribute'}),

#             'label_5': forms.TextInput(attrs={'class':'form-control fw-bold', 'placeholder':'Enter Name of Test Attribute'}),
#             'value_5': forms.TextInput(attrs={'class':'form-control fw-bold', 'placeholder':'Enter Value of Test Attribute'}),

#             'label_6': forms.TextInput(attrs={'class':'form-control fw-bold', 'placeholder':'Enter Name of Test Attribute'}),
#             'value_6': forms.TextInput(attrs={'class':'form-control fw-bold', 'placeholder':'Enter Value of Test Attribute'}),

#             'label_7': forms.TextInput(attrs={'class':'form-control fw-bold', 'placeholder':'Enter Name of Test Attribute'}),
#             'value_7': forms.TextInput(attrs={'class':'form-control fw-bold', 'placeholder':'Enter Value of Test Attribute'}),

#             'label_8': forms.TextInput(attrs={'class':'form-control fw-bold', 'placeholder':'Enter Name of Test Attribute'}),
#             'value_8': forms.TextInput(attrs={'class':'form-control fw-bold', 'placeholder':'Enter Value of Test Attribute'}),

#             'label_9': forms.TextInput(attrs={'class':'form-control fw-bold', 'placeholder':'Enter Name of Test Attribute'}),
#             'value_9': forms.TextInput(attrs={'class':'form-control fw-bold', 'placeholder':'Enter Value of Test Attribute'}),

#             'label_10': forms.TextInput(attrs={'class':'form-control fw-bold', 'placeholder':'Enter Name of Test Attribute'}),
#             'value_10': forms.TextInput(attrs={'class':'form-control fw-bold', 'placeholder':'Enter Value of Test Attribute'}),

#             'label_11': forms.TextInput(attrs={'class':'form-control fw-bold', 'placeholder':'Enter Name of Test Attribute'}),
#             'value_11': forms.TextInput(attrs={'class':'form-control fw-bold', 'placeholder':'Enter Value of Test Attribute'}),

#             'label_12': forms.TextInput(attrs={'class':'form-control fw-bold', 'placeholder':'Enter Name of Test Attribute'}),
#             'value_12': forms.TextInput(attrs={'class':'form-control fw-bold', 'placeholder':'Enter Value of Test Attribute'}),

#             'label_13': forms.TextInput(attrs={'class':'form-control fw-bold', 'placeholder':'Enter Name of Test Attribute'}),
#             'value_13': forms.TextInput(attrs={'class':'form-control fw-bold', 'placeholder':'Enter Value of Test Attribute'}),

#             'label_14': forms.TextInput(attrs={'class':'form-control fw-bold', 'placeholder':'Enter Name of Test Attribute'}),
#             'value_14': forms.TextInput(attrs={'class':'form-control fw-bold', 'placeholder':'Enter Value of Test Attribute'}),

#             'label_15': forms.TextInput(attrs={'class':'form-control fw-bold', 'placeholder':'Enter Name of Test Attribute'}),
#             'value_15': forms.TextInput(attrs={'class':'form-control fw-bold', 'placeholder':'Enter Value of Test Attribute'}),

#             'label_16': forms.TextInput(attrs={'class':'form-control fw-bold', 'placeholder':'Enter Name of Test Attribute'}),
#             'value_16': forms.TextInput(attrs={'class':'form-control fw-bold', 'placeholder':'Enter Value of Test Attribute'}),

#             'label_17': forms.TextInput(attrs={'class':'form-control fw-bold', 'placeholder':'Enter Name of Test Attribute'}),
#             'value_17': forms.TextInput(attrs={'class':'form-control fw-bold', 'placeholder':'Enter Value of Test Attribute'}),

#             'label_18': forms.TextInput(attrs={'class':'form-control fw-bold', 'placeholder':'Enter Name of Test Attribute'}),
#             'value_18': forms.TextInput(attrs={'class':'form-control fw-bold', 'placeholder':'Enter Value of Test Attribute'}),

#             'label_19': forms.TextInput(attrs={'class':'form-control fw-bold', 'placeholder':'Enter Name of Test Attribute'}),
#             'value_19': forms.TextInput(attrs={'class':'form-control fw-bold', 'placeholder':'Enter Value of Test Attribute'}),

#             'label_20': forms.TextInput(attrs={'class':'form-control fw-bold', 'placeholder':'Enter Name of Test Attribute'}),
#             'value_20': forms.TextInput(attrs={'class':'form-control fw-bold', 'placeholder':'Enter Value of Test Attribute'}),

#             'label_21': forms.TextInput(attrs={'class':'form-control fw-bold', 'placeholder':'Enter Name of Test Attribute'}),
#             'value_21': forms.TextInput(attrs={'class':'form-control fw-bold', 'placeholder':'Enter Value of Test Attribute'}),

#             'label_22': forms.TextInput(attrs={'class':'form-control fw-bold', 'placeholder':'Enter Name of Test Attribute'}),
#             'value_22': forms.TextInput(attrs={'class':'form-control fw-bold', 'placeholder':'Enter Value of Test Attribute'}),

#             'label_23': forms.TextInput(attrs={'class':'form-control fw-bold', 'placeholder':'Enter Name of Test Attribute'}),
#             'value_23': forms.TextInput(attrs={'class':'form-control fw-bold', 'placeholder':'Enter Value of Test Attribute'}),

#             'label_24': forms.TextInput(attrs={'class':'form-control fw-bold', 'placeholder':'Enter Name of Test Attribute'}),
#             'value_24': forms.TextInput(attrs={'class':'form-control fw-bold', 'placeholder':'Enter Value of Test Attribute'}),

#             'label_25': forms.TextInput(attrs={'class':'form-control fw-bold', 'placeholder':'Enter Name of Test Attribute'}),
#             'value_25': forms.TextInput(attrs={'class':'form-control fw-bold', 'placeholder':'Enter Value of Test Attribute'}),

#             'label_26': forms.TextInput(attrs={'class':'form-control fw-bold', 'placeholder':'Enter Name of Test Attribute'}),
#             'value_26': forms.TextInput(attrs={'class':'form-control fw-bold', 'placeholder':'Enter Value of Test Attribute'}),

#             'label_27': forms.TextInput(attrs={'class':'form-control fw-bold', 'placeholder':'Enter Name of Test Attribute'}),
#             'value_27': forms.TextInput(attrs={'class':'form-control fw-bold', 'placeholder':'Enter Value of Test Attribute'}),

#             'label_28': forms.TextInput(attrs={'class':'form-control fw-bold', 'placeholder':'Enter Name of Test Attribute'}),
#             'value_28': forms.TextInput(attrs={'class':'form-control fw-bold', 'placeholder':'Enter Value of Test Attribute'}),

#             'label_29': forms.TextInput(attrs={'class':'form-control fw-bold', 'placeholder':'Enter Name of Test Attribute'}),
#             'value_29': forms.TextInput(attrs={'class':'form-control fw-bold', 'placeholder':'Enter Value of Test Attribute'}),


#             'label_30': forms.TextInput(attrs={'class':'form-control fw-bold', 'placeholder':'Enter Name of Test Attribute'}),
#             'value_30': forms.TextInput(attrs={'class':'form-control fw-bold', 'placeholder':'Enter Value of Test Attribute'}),

#             'label_31': forms.TextInput(attrs={'class':'form-control fw-bold', 'placeholder':'Enter Name of Test Attribute'}),
#             'value_31': forms.TextInput(attrs={'class':'form-control fw-bold', 'placeholder':'Enter Value of Test Attribute'}),

#             'label_32': forms.TextInput(attrs={'class':'form-control fw-bold', 'placeholder':'Enter Name of Test Attribute'}),
#             'value_32': forms.TextInput(attrs={'class':'form-control fw-bold', 'placeholder':'Enter Value of Test Attribute'}),

#             'label_33': forms.TextInput(attrs={'class':'form-control fw-bold', 'placeholder':'Enter Name of Test Attribute'}),
#             'value_33': forms.TextInput(attrs={'class':'form-control fw-bold', 'placeholder':'Enter Value of Test Attribute'}),

#             'label_34': forms.TextInput(attrs={'class':'form-control fw-bold', 'placeholder':'Enter Name of Test Attribute'}),
#             'value_34': forms.TextInput(attrs={'class':'form-control fw-bold', 'placeholder':'Enter Value of Test Attribute'}),

#             'label_35': forms.TextInput(attrs={'class':'form-control fw-bold', 'placeholder':'Enter Name of Test Attribute'}),
#             'value_35': forms.TextInput(attrs={'class':'form-control fw-bold', 'placeholder':'Enter Value of Test Attribute'}),

#             'label_36': forms.TextInput(attrs={'class':'form-control fw-bold', 'placeholder':'Enter Name of Test Attribute'}),
#             'value_36': forms.TextInput(attrs={'class':'form-control fw-bold', 'placeholder':'Enter Value of Test Attribute'}),

#             'label_37': forms.TextInput(attrs={'class':'form-control fw-bold', 'placeholder':'Enter Name of Test Attribute'}),
#             'value_37': forms.TextInput(attrs={'class':'form-control fw-bold', 'placeholder':'Enter Value of Test Attribute'}),

#             'label_38': forms.TextInput(attrs={'class':'form-control fw-bold', 'placeholder':'Enter Name of Test Attribute'}),
#             'value_38': forms.TextInput(attrs={'class':'form-control fw-bold', 'placeholder':'Enter Value of Test Attribute'}),

#             'label_39': forms.TextInput(attrs={'class':'form-control fw-bold', 'placeholder':'Enter Name of Test Attribute'}),
#             'value_39': forms.TextInput(attrs={'class':'form-control fw-bold', 'placeholder':'Enter Value of Test Attribute'}),

#             'label_40': forms.TextInput(attrs={'class':'form-control fw-bold', 'placeholder':'Enter Name of Test Attribute'}),
#             'value_40': forms.TextInput(attrs={'class':'form-control fw-bold', 'placeholder':'Enter Value of Test Attribute'}),

#             'label_41': forms.TextInput(attrs={'class':'form-control fw-bold', 'placeholder':'Enter Name of Test Attribute'}),
#             'value_41': forms.TextInput(attrs={'class':'form-control fw-bold', 'placeholder':'Enter Value of Test Attribute'}),

#             'label_42': forms.TextInput(attrs={'class':'form-control fw-bold', 'placeholder':'Enter Name of Test Attribute'}),
#             'value_42': forms.TextInput(attrs={'class':'form-control fw-bold', 'placeholder':'Enter Value of Test Attribute'}),

#             'label_43': forms.TextInput(attrs={'class':'form-control fw-bold', 'placeholder':'Enter Name of Test Attribute'}),
#             'value_43': forms.TextInput(attrs={'class':'form-control fw-bold', 'placeholder':'Enter Value of Test Attribute'}),

#             'label_44': forms.TextInput(attrs={'class':'form-control fw-bold', 'placeholder':'Enter Name of Test Attribute'}),
#             'value_44': forms.TextInput(attrs={'class':'form-control fw-bold', 'placeholder':'Enter Value of Test Attribute'}),

#             'label_45': forms.TextInput(attrs={'class':'form-control fw-bold', 'placeholder':'Enter Name of Test Attribute'}),
#             'value_45': forms.TextInput(attrs={'class':'form-control fw-bold', 'placeholder':'Enter Value of Test Attribute'}),

#             'label_46': forms.TextInput(attrs={'class':'form-control fw-bold', 'placeholder':'Enter Name of Test Attribute'}),
#             'value_46': forms.TextInput(attrs={'class':'form-control fw-bold', 'placeholder':'Enter Value of Test Attribute'}),

#             'label_47': forms.TextInput(attrs={'class':'form-control fw-bold', 'placeholder':'Enter Name of Test Attribute'}),
#             'value_47': forms.TextInput(attrs={'class':'form-control fw-bold', 'placeholder':'Enter Value of Test Attribute'}),

#             'label_48': forms.TextInput(attrs={'class':'form-control fw-bold', 'placeholder':'Enter Name of Test Attribute'}),
#             'value_48': forms.TextInput(attrs={'class':'form-control fw-bold', 'placeholder':'Enter Value of Test Attribute'}),

#             'label_49': forms.TextInput(attrs={'class':'form-control fw-bold', 'placeholder':'Enter Name of Test Attribute'}),
#             'value_49': forms.TextInput(attrs={'class':'form-control fw-bold', 'placeholder':'Enter Value of Test Attribute'}),

#             'label_50': forms.TextInput(attrs={'class':'form-control fw-bold', 'placeholder':'Enter Name of Test Attribute'}),
#             'value_50': forms.TextInput(attrs={'class':'form-control fw-bold', 'placeholder':'Enter Value of Test Attribute'}),
#         }