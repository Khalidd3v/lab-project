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
        ('Stool RE Test', 'Stool RE Test'),
        ('Urine RE Test', 'Urine RE Test'),
        ('Serology Test', 'Serology Test'),
        ('Semen Test', 'Semen Test'),
        ('CRP Test', 'CRP Test'),
        ('Thyroid Test', 'Thyroid Test'),
        ('Kedney Function Test', 'Kedney Function Test'),
        ('Liver Function Test', 'Liver Function Test'),
        ('Glucose BF Test', 'Glucose BF Test'),
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
# urine_re Test Form

class UrineRETestForm(forms.ModelForm):
    class Meta:
        model = UrineReTest
        fields = '__all__'
        exclude = ['patient']
        widgets = {

            
            'ph': forms.TextInput(attrs={'class':'form-control fw-bold', 'placeholder':'Enter Value'}),
            'sugar': forms.TextInput(attrs={'class':'form-control fw-bold', 'placeholder':'Enter Value'}),
            'albumin': forms.TextInput(attrs={'class':'form-control fw-bold', 'placeholder':'Enter Value'}),
            'm_puss_cells': forms.TextInput(attrs={'class':'form-control fw-bold', 'placeholder':'Enter Value'}),
            'rbcs': forms.TextInput(attrs={'class':'form-control fw-bold', 'placeholder':'Enter Value'}),
            'epth_cells': forms.TextInput(attrs={'class':'form-control fw-bold', 'placeholder':'Enter Value'}),
            'casts': forms.TextInput(attrs={'class':'form-control fw-bold', 'placeholder':'Enter Value'}),
            'ca_oxalate': forms.TextInput(attrs={'class':'form-control fw-bold', 'placeholder':'Enter Value'}),
            'm_backteria': forms.TextInput(attrs={'class':'form-control fw-bold', 'placeholder':'Enter Value'}),
            'other': forms.TextInput(attrs={'class':'form-control fw-bold', 'placeholder':'Enter Value'}),
            'urine_protien': forms.TextInput(attrs={'class':'form-control fw-bold', 'placeholder':'Enter Value'}),


        }


# Serology Test Form

class SerologyTestForm(forms.ModelForm):
    class Meta:
        model = SerologyTest
        fields = '__all__'
        exclude = ['patient']
        widgets = {

            
            'twenty': forms.TextInput(attrs={'class':'form-control fw-bold', 'placeholder':'Enter Value'}),
            'fourty': forms.TextInput(attrs={'class':'form-control fw-bold', 'placeholder':'Enter Value'}),
            'sixty': forms.TextInput(attrs={'class':'form-control fw-bold', 'placeholder':'Enter Value'}),
            'one_sixty': forms.TextInput(attrs={'class':'form-control fw-bold', 'placeholder':'Enter Value'}),
            'three_twenty': forms.TextInput(attrs={'class':'form-control fw-bold', 'placeholder':'Enter Value'}),
            'th': forms.TextInput(attrs={'class':'form-control fw-bold', 'placeholder':'Enter Value'}),
            'dilution': forms.TextInput(attrs={'class':'form-control fw-bold', 'placeholder':'Enter Value'}),
            'ba': forms.TextInput(attrs={'class':'form-control fw-bold', 'placeholder':'Enter Value'}),
            'bm': forms.TextInput(attrs={'class':'form-control fw-bold', 'placeholder':'Enter Value'}),
            'th_twenty': forms.TextInput(attrs={'class':'form-control fw-bold', 'placeholder':'Enter Value'}),
            'th_fourty': forms.TextInput(attrs={'class':'form-control fw-bold', 'placeholder':'Enter Value'}),
            'th_sixty': forms.TextInput(attrs={'class':'form-control fw-bold', 'placeholder':'Enter Value'}),
            'th_one_sixty': forms.TextInput(attrs={'class':'form-control fw-bold', 'placeholder':'Enter Value'}),
            'th_three_twenty': forms.TextInput(attrs={'class':'form-control fw-bold', 'placeholder':'Enter Value'}),
            'dil_twenty': forms.TextInput(attrs={'class':'form-control fw-bold', 'placeholder':'Enter Value'}),
            'dil_fourty': forms.TextInput(attrs={'class':'form-control fw-bold', 'placeholder':'Enter Value'}),
            'dil_sixty': forms.TextInput(attrs={'class':'form-control fw-bold', 'placeholder':'Enter Value'}),
            'dil_one_sixty': forms.TextInput(attrs={'class':'form-control fw-bold', 'placeholder':'Enter Value'}),
            'dil_three_twenty': forms.TextInput(attrs={'class':'form-control fw-bold', 'placeholder':'Enter Value'}),
            'ba_twenty': forms.TextInput(attrs={'class':'form-control fw-bold', 'placeholder':'Enter Value'}),
            'ba_fourty': forms.TextInput(attrs={'class':'form-control fw-bold', 'placeholder':'Enter Value'}),
            'ba_sixty': forms.TextInput(attrs={'class':'form-control fw-bold', 'placeholder':'Enter Value'}),
            'ba_one_sixty': forms.TextInput(attrs={'class':'form-control fw-bold', 'placeholder':'Enter Value'}),
            'ba_three_twenty': forms.TextInput(attrs={'class':'form-control fw-bold', 'placeholder':'Enter Value'}),
            'bm_twenty': forms.TextInput(attrs={'class':'form-control fw-bold', 'placeholder':'Enter Value'}),
            'bm_fourty': forms.TextInput(attrs={'class':'form-control fw-bold', 'placeholder':'Enter Value'}),
            'bm_sixty': forms.TextInput(attrs={'class':'form-control fw-bold', 'placeholder':'Enter Value'}),
            'bm_one_sixty': forms.TextInput(attrs={'class':'form-control fw-bold', 'placeholder':'Enter Value'}),
            'bm_three_twenty': forms.TextInput(attrs={'class':'form-control fw-bold', 'placeholder':'Enter Value'}),
            'ig_taxo': forms.TextInput(attrs={'class':'form-control fw-bold', 'placeholder':'Enter Value'}),
            'igm_taxo': forms.TextInput(attrs={'class':'form-control fw-bold', 'placeholder':'Enter Value'}),
            'vdrl': forms.TextInput(attrs={'class':'form-control fw-bold', 'placeholder':'Enter Value'}),
            'hbs_ag': forms.TextInput(attrs={'class':'form-control fw-bold', 'placeholder':'Enter Value'}),
            'hcv_ab': forms.TextInput(attrs={'class':'form-control fw-bold', 'placeholder':'Enter Value'}),
            'hiv_aids': forms.TextInput(attrs={'class':'form-control fw-bold', 'placeholder':'Enter Value'}),
            'aso_titre': forms.TextInput(attrs={'class':'form-control fw-bold', 'placeholder':'Enter Value'}),
            'ra_factor': forms.TextInput(attrs={'class':'form-control fw-bold', 'placeholder':'Enter Value'}),
            'h_pylori': forms.TextInput(attrs={'class':'form-control fw-bold', 'placeholder':'Enter Value'}),
            'tb_ict': forms.TextInput(attrs={'class':'form-control fw-bold', 'placeholder':'Enter Value'}),
            'typhiod_ig': forms.TextInput(attrs={'class':'form-control fw-bold', 'placeholder':'Enter Value'}),
            'typhiod_igm': forms.TextInput(attrs={'class':'form-control fw-bold', 'placeholder':'Enter Value'}),
            'dangue_ns1': forms.TextInput(attrs={'class':'form-control fw-bold', 'placeholder':'Enter Value'}),
            'dangue_ig': forms.TextInput(attrs={'class':'form-control fw-bold', 'placeholder':'Enter Value'}),
            'dangue_igm': forms.TextInput(attrs={'class':'form-control fw-bold', 'placeholder':'Enter Value'}),
            'bloodgroup': forms.TextInput(attrs={'class':'form-control fw-bold', 'placeholder':'Enter Value'}),
            'rh_factor': forms.TextInput(attrs={'class':'form-control fw-bold', 'placeholder':'Enter Value'}),
            'cross_match': forms.TextInput(attrs={'class':'form-control fw-bold', 'placeholder':'Enter Value'}),
            'pregnancy': forms.TextInput(attrs={'class':'form-control fw-bold', 'placeholder':'Enter Value'}),


        }

# Semen Test Form

class SemenTestForm(forms.ModelForm):
    class Meta:
        model = SemenTest
        fields = '__all__'
        exclude = ['patient']
        widgets = {

            
            'total_sperm': forms.TextInput(attrs={'class':'form-control fw-bold', 'placeholder':'Enter Value'}),
            'ejaculate_volume': forms.TextInput(attrs={'class':'form-control fw-bold', 'placeholder':'Enter Value'}),
            'sperm_concentration': forms.TextInput(attrs={'class':'form-control fw-bold', 'placeholder':'Enter Value'}),
            'total_motility': forms.TextInput(attrs={'class':'form-control fw-bold', 'placeholder':'Enter Value'}),
            'progressive_motility': forms.TextInput(attrs={'class':'form-control fw-bold', 'placeholder':'Enter Value'}),
            'sperm_morphology': forms.TextInput(attrs={'class':'form-control fw-bold', 'placeholder':'Enter Value'}),

        }
# CRP Test Form

class CRPTestForm(forms.ModelForm):
    class Meta:
        model = CRPTest
        fields = '__all__'
        exclude = ['patient']
        widgets = {

            
            'crps': forms.TextInput(attrs={'class':'form-control fw-bold', 'placeholder':'Enter Value'}),


        }

# Thyroid Test Form

class ThyroidTestForm(forms.ModelForm):
    class Meta:
        model = ThyroidTest
        fields = '__all__'
        exclude = ['patient']
        widgets = {

            
            'tsh': forms.TextInput(attrs={'class':'form-control fw-bold', 'placeholder':'Enter Value'}),
            't4': forms.TextInput(attrs={'class':'form-control fw-bold', 'placeholder':'Enter Value'}),
            't4_free': forms.TextInput(attrs={'class':'form-control fw-bold', 'placeholder':'Enter Value'}),
            't3': forms.TextInput(attrs={'class':'form-control fw-bold', 'placeholder':'Enter Value'}),
            't3_free': forms.TextInput(attrs={'class':'form-control fw-bold', 'placeholder':'Enter Value'}),
            'reverse_t3': forms.TextInput(attrs={'class':'form-control fw-bold', 'placeholder':'Enter Value'}),
            'anti_thyrog_antibody': forms.TextInput(attrs={'class':'form-control fw-bold', 'placeholder':'Enter Value'}),
            'anti_thyrog_peroxidase': forms.TextInput(attrs={'class':'form-control fw-bold', 'placeholder':'Enter Value'}),


        }

# Kedney Funtion Test Form

class KedneyFunctionTestForm(forms.ModelForm):
    class Meta:
        model = KedneyFunctionTest
        fields = '__all__'
        exclude = ['patient']
        widgets = {

            
            'bun': forms.TextInput(attrs={'class':'form-control fw-bold', 'placeholder':'Enter Value'}),
            'cr': forms.TextInput(attrs={'class':'form-control fw-bold', 'placeholder':'Enter Value'}),
            'ua': forms.TextInput(attrs={'class':'form-control fw-bold', 'placeholder':'Enter Value'}),
            'ca': forms.TextInput(attrs={'class':'form-control fw-bold', 'placeholder':'Enter Value'}),
            'k': forms.TextInput(attrs={'class':'form-control fw-bold', 'placeholder':'Enter Value'}),
            'na': forms.TextInput(attrs={'class':'form-control fw-bold', 'placeholder':'Enter Value'}),
            'co2_cp': forms.TextInput(attrs={'class':'form-control fw-bold', 'placeholder':'Enter Value'}),
            'cl': forms.TextInput(attrs={'class':'form-control fw-bold', 'placeholder':'Enter Value'}),
            'fe': forms.TextInput(attrs={'class':'form-control fw-bold', 'placeholder':'Enter Value'}),
            'mg': forms.TextInput(attrs={'class':'form-control fw-bold', 'placeholder':'Enter Value'}),
            'zn': forms.TextInput(attrs={'class':'form-control fw-bold', 'placeholder':'Enter Value'}),
            'p': forms.TextInput(attrs={'class':'form-control fw-bold', 'placeholder':'Enter Value'}),


        }

# Liver Function Test Form

class LiverFunctionTestForm(forms.ModelForm):
    class Meta:
        model = LiverFunctionTest
        fields = '__all__'
        exclude = ['patient']
        widgets = {

            
            'alt_gpt': forms.TextInput(attrs={'class':'form-control fw-bold', 'placeholder':'Enter Value'}),
            'ast_got': forms.TextInput(attrs={'class':'form-control fw-bold', 'placeholder':'Enter Value'}),
            'acp': forms.TextInput(attrs={'class':'form-control fw-bold', 'placeholder':'Enter Value'}),
            'alp': forms.TextInput(attrs={'class':'form-control fw-bold', 'placeholder':'Enter Value'}),
            't_bil': forms.TextInput(attrs={'class':'form-control fw-bold', 'placeholder':'Enter Value'}),
            'd_bil': forms.TextInput(attrs={'class':'form-control fw-bold', 'placeholder':'Enter Value'}),
            'che': forms.TextInput(attrs={'class':'form-control fw-bold', 'placeholder':'Enter Value'}),
            'tp': forms.TextInput(attrs={'class':'form-control fw-bold', 'placeholder':'Enter Value'}),
            'alb': forms.TextInput(attrs={'class':'form-control fw-bold', 'placeholder':'Enter Value'}),
            'fb': forms.TextInput(attrs={'class':'form-control fw-bold', 'placeholder':'Enter Value'}),
            'nhs': forms.TextInput(attrs={'class':'form-control fw-bold', 'placeholder':'Enter Value'}),
            'y_gt': forms.TextInput(attrs={'class':'form-control fw-bold', 'placeholder':'Enter Value'}),
            'ttt': forms.TextInput(attrs={'class':'form-control fw-bold', 'placeholder':'Enter Value'}),


        }


# Glucose BF Test Form

class GlucoseBFTestForm(forms.ModelForm):
    class Meta:
        model = Glucose_BFTest
        fields = '__all__'
        exclude = ['patient']
        widgets = {

            
            'glu': forms.TextInput(attrs={'class':'form-control fw-bold', 'placeholder':'Enter Value'}),
            'apo_a1': forms.TextInput(attrs={'class':'form-control fw-bold', 'placeholder':'Enter Value'}),
            'tg': forms.TextInput(attrs={'class':'form-control fw-bold', 'placeholder':'Enter Value'}),
            'hdl_c': forms.TextInput(attrs={'class':'form-control fw-bold', 'placeholder':'Enter Value'}),
            'ldl_c': forms.TextInput(attrs={'class':'form-control fw-bold', 'placeholder':'Enter Value'}),
            'hbaic_g': forms.TextInput(attrs={'class':'form-control fw-bold', 'placeholder':'Enter Value'}),
            'apo_b': forms.TextInput(attrs={'class':'form-control fw-bold', 'placeholder':'Enter Value'}),
            't_cho': forms.TextInput(attrs={'class':'form-control fw-bold', 'placeholder':'Enter Value'}),



        }






