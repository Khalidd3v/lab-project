from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User



class MyImage(models.Model):
    image = models.ImageField(upload_to='images/')
    caption = models.CharField(max_length=100)



class Doctor(models.Model):
    name = models.CharField(max_length=32)
    address = models.CharField( blank=True ,max_length=50)
    phone_number = models.CharField(max_length=13,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name



#Selected Test Model



Patient_Gender = (("male","male"), ("female","female"))

class Patient(models.Model):
    
    doctor = models.ForeignKey(Doctor, on_delete=models.DO_NOTHING)
    name = models.CharField(max_length=32)
    gender = models.CharField(choices=Patient_Gender, default="Male", max_length=10)
    age = models.IntegerField()
    report_date = models.DateTimeField(default=timezone.now)
    update_at = models.DateTimeField(auto_now=True)
    address = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    



# #CBC TEST

class CBCTest(models.Model):
    
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    Haemoglobin1 = models.CharField(max_length=20, blank=True)
    Total_RBC = models.CharField(max_length=20, blank=True)
    HCT = models.CharField(max_length=20, blank=True)
    MCV = models.CharField(max_length=20, blank=True)
    MCH = models.CharField(max_length=20, blank=True)
    MCHC = models.CharField(max_length=20, blank=True)
    Total_WBC = models.CharField(max_length=20, blank=True)
    Neutrophils = models.CharField(max_length=20, blank=True)
    Lymphocytes = models.CharField(max_length=20, blank=True)
    Monocytes = models.CharField(max_length=20, blank=True)
    Eosonophils = models.CharField(max_length=20, blank=True)
    Platelet = models.CharField(max_length=20, blank=True)
    Basophils = models.CharField(max_length=20, blank=True)
    ESR = models.CharField(max_length=20, blank=True)


# biochemistry test
class BioChemistryTest(models.Model):
    
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    hba1c = models.CharField(max_length=20, blank=True)
    b_sugar_r = models.CharField(max_length=20, blank=True)
    b_sugar_f = models.CharField(max_length=20, blank=True)
    sgpt_alt = models.CharField(max_length=20, blank=True)
    sgot_ast = models.CharField(max_length=20, blank=True)
    alk_phosphatase = models.CharField(max_length=20, blank=True)
    sbillirubin_total = models.CharField(max_length=20, blank=True)
    sbillirubin_direct = models.CharField(max_length=20, blank=True)
    sbillirubin_indirect = models.CharField(max_length=20, blank=True)
    s_calium = models.CharField(max_length=20, blank=True)
    s_uric_acid = models.CharField(max_length=20, blank=True)
    b_urea = models.CharField(max_length=20, blank=True)
    s_creatinine = models.CharField(max_length=20, blank=True)
    s_amylase = models.CharField(max_length=20, blank=True)
    s_cholestrol = models.CharField(max_length=20, blank=True)
    triglycerides = models.CharField(max_length=20, blank=True)
    hdl = models.CharField(max_length=20, blank=True)
    ldl = models.CharField(max_length=20, blank=True)
    ldh = models.CharField(max_length=20, blank=True)
    t_protien = models.CharField(max_length=20, blank=True)
    cpk = models.CharField(max_length=20, blank=True)
    crp = models.CharField(max_length=20, blank=True)
    
# stool r/e  
class StoolRETest(models.Model):
    
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    color = models.CharField(max_length=20, blank=True)
    mucus = models.CharField(max_length=20, blank=True)
    ova = models.CharField(max_length=20, blank=True)
    cyst = models.CharField(max_length=20, blank=True)
    puss_cells = models.CharField(max_length=20, blank=True)
    rbcs = models.CharField(max_length=20, blank=True)
    backteria = models.CharField(max_length=20, blank=True)
    stool_hpylori = models.CharField(max_length=20, blank=True)


# urine_re
class UrineReTest(models.Model):
    
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    ph = models.CharField(max_length=20, blank=True)
    sugar = models.CharField(max_length=20, blank=True)
    albumin = models.CharField(max_length=20, blank=True)
    m_puss_cells = models.CharField(max_length=20, blank=True)
    rbcs = models.CharField(max_length=20, blank=True)
    epth_cells = models.CharField(max_length=20, blank=True)
    casts = models.CharField(max_length=20, blank=True)
    ca_oxalate = models.CharField(max_length=20, blank=True)
    m_backteria = models.CharField(max_length=20, blank=True)
    other = models.CharField(max_length=20, blank=True)
    urine_protien = models.CharField(max_length=20, blank=True)


#serology
class SerologyTest(models.Model):
    
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    twenty = models.CharField(max_length=20, blank=True)
    fourty = models.CharField(max_length=20, blank=True)
    sixty = models.CharField(max_length=20, blank=True)
    one_sixty = models.CharField(max_length=20, blank=True)
    three_twenty = models.CharField(max_length=20, blank=True)
    
    th = models.CharField(max_length=20, blank=True)
    dilution = models.CharField(max_length=20, blank=True)
    ba = models.CharField(max_length=20, blank=True)
    bm = models.CharField(max_length=20, blank=True)

    th_twenty = models.CharField(max_length=20, blank=True)
    th_fourty = models.CharField(max_length=20, blank=True)
    th_sixty = models.CharField(max_length=20, blank=True)
    th_one_sixty = models.CharField(max_length=20, blank=True)
    th_three_twenty = models.CharField(max_length=20, blank=True)

    dil_twenty = models.CharField(max_length=20, blank=True)
    dil_fourty = models.CharField(max_length=20, blank=True)
    dil_sixty = models.CharField(max_length=20, blank=True)
    dil_one_sixty = models.CharField(max_length=20, blank=True)
    dil_three_twenty = models.CharField(max_length=20, blank=True)

    ba_twenty = models.CharField(max_length=20, blank=True)
    ba_fourty = models.CharField(max_length=20, blank=True)
    ba_sixty = models.CharField(max_length=20, blank=True)
    ba_one_sixty = models.CharField(max_length=20, blank=True)
    ba_three_twenty = models.CharField(max_length=20, blank=True)

    bm_twenty = models.CharField(max_length=20, blank=True)
    bm_fourty = models.CharField(max_length=20, blank=True)
    bm_sixty = models.CharField(max_length=20, blank=True)
    bm_one_sixty = models.CharField(max_length=20, blank=True)
    bm_three_twenty = models.CharField(max_length=20, blank=True)

    ig_taxo = models.CharField(max_length=20, blank=True)
    igm_taxo = models.CharField(max_length=20, blank=True)

    vdrl = models.CharField(max_length=20, blank=True)
    hbs_ag = models.CharField(max_length=20, blank=True)
    hcv_ab = models.CharField(max_length=20, blank=True)
    hiv_aids = models.CharField(max_length=20, blank=True)
    aso_titre = models.CharField(max_length=20, blank=True)
    ra_factor = models.CharField(max_length=20, blank=True)
    h_pylori = models.CharField(max_length=20, blank=True)
    tb_ict = models.CharField(max_length=20, blank=True)
    typhiod_ig = models.CharField(max_length=20, blank=True)
    typhiod_igm = models.CharField(max_length=20, blank=True)
    dangue_ns1 = models.CharField(max_length=20, blank=True)
    dangue_ig = models.CharField(max_length=20, blank=True)
    dangue_igm = models.CharField(max_length=20, blank=True)
    bloodgroup = models.CharField(max_length=20, blank=True)
    rh_factor = models.CharField(max_length=20, blank=True)
    cross_match = models.CharField(max_length=20, blank=True)
    pregnancy = models.CharField(max_length=20, blank=True)

# semen 
class SemenTest(models.Model):
    
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    total_sperm = models.CharField(max_length=20, blank=True)
    ejaculate_volume = models.CharField(max_length=20, blank=True)
    sperm_concentration = models.CharField(max_length=20, blank=True)
    total_motility = models.CharField(max_length=20, blank=True)
    progressive_motility = models.CharField(max_length=20, blank=True)
    sperm_morphology = models.CharField(max_length=20, blank=True)

# crp 
class CRPTest(models.Model):
    
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    crps = models.CharField(max_length=20, blank=True)

# thyroid
class ThyroidTest(models.Model):
    
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    tsh = models.CharField(max_length=20, blank=True)
    t4 = models.CharField(max_length=20, blank=True)
    t4_free = models.CharField(max_length=20, blank=True)
    t3 = models.CharField(max_length=20, blank=True)
    t3_free = models.CharField(max_length=20, blank=True)
    reverse_t3 = models.CharField(max_length=20, blank=True)
    anti_thyrog_antibody = models.CharField(max_length=20, blank=True)
    anti_thyrog_peroxidase = models.CharField(max_length=20, blank=True)

# kedney function test
class KedneyFunctionTest(models.Model):
    
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    bun = models.CharField(max_length=20, blank=True)
    cr = models.CharField(max_length=20, blank=True)
    ua = models.CharField(max_length=20, blank=True)
    ca = models.CharField(max_length=20, blank=True)
    k = models.CharField(max_length=20, blank=True)
    na = models.CharField(max_length=20, blank=True)
    co2_cp = models.CharField(max_length=20, blank=True)
    cl = models.CharField(max_length=20, blank=True)
    fe = models.CharField(max_length=20, blank=True)
    mg = models.CharField(max_length=20, blank=True)
    zn = models.CharField(max_length=20, blank=True)
    p = models.CharField(max_length=20, blank=True)
    
# Liver Function
class LiverFunctionTest(models.Model):

    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    alt_gpt = models.CharField(max_length=20, blank=True)
    ast_got = models.CharField(max_length=20, blank=True)
    acp = models.CharField(max_length=20, blank=True)
    alp = models.CharField(max_length=20, blank=True)
    t_bil= models.CharField(max_length=20, blank=True)
    d_bil = models.CharField(max_length=20, blank=True)
    che = models.CharField(max_length=20, blank=True)
    tp = models.CharField(max_length=20, blank=True)
    alb = models.CharField(max_length=20, blank=True)
    fb = models.CharField(max_length=20, blank=True)
    nhs = models.CharField(max_length=20, blank=True)
    y_gt = models.CharField(max_length=20, blank=True)
    ttt = models.CharField(max_length=20, blank=True)

# Glucose_BF Test Model
class Glucose_BFTest(models.Model):

    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    glu = models.CharField(max_length=20, blank=True)
    apo_a1 = models.CharField(max_length=20, blank=True)
    tg = models.CharField(max_length=20, blank=True)
    hdl_c = models.CharField(max_length=20, blank=True)
    ldl_c = models.CharField(max_length=20, blank=True)
    hbaic_g = models.CharField(max_length=20, blank=True)
    apo_b = models.CharField(max_length=20, blank=True)
    t_cho = models.CharField(max_length=20, blank=True)


# # #main test models 

# class Tests(models.Model):
#     patient = models.ForeignKey(Patient, on_delete=models.Case, blank=True, null=True, default="")
#     identifier = models.CharField(max_length=100, blank=False)

#     label_1 = models.CharField(max_length=32, blank=True, null=True)
#     value_1 = models.CharField(max_length=32, blank=True, null=True)

#     label_2 = models.CharField(max_length=32, blank=True, null=True)
#     value_2 = models.CharField(max_length=32, blank=True, null=True)

#     label_3 = models.CharField(max_length=32, blank=True, null=True)
#     value_3 = models.CharField(max_length=32, blank=True, null=True)

#     label_4 = models.CharField(max_length=32, blank=True, null=True)
#     value_4 = models.CharField(max_length=32, blank=True, null=True)

#     label_5 = models.CharField(max_length=32, blank=True, null=True)
#     value_5 = models.CharField(max_length=32, blank=True, null=True)

#     label_6 = models.CharField(max_length=32, blank=True, null=True)
#     value_6 = models.CharField(max_length=32, blank=True, null=True)

#     label_7 = models.CharField(max_length=32, blank=True, null=True)
#     value_7 = models.CharField(max_length=32, blank=True, null=True)

#     label_8 = models.CharField(max_length=32, blank=True, null=True)
#     value_8 = models.CharField(max_length=32, blank=True, null=True)

#     label_9 = models.CharField(max_length=32, blank=True, null=True)
#     value_9 = models.CharField(max_length=32, blank=True, null=True)

#     label_10 = models.CharField(max_length=32, blank=True, null=True)
#     value_10 = models.CharField(max_length=32, blank=True, null=True)

#     label_11 = models.CharField(max_length=32, blank=True, null=True)
#     value_11 = models.CharField(max_length=32, blank=True, null=True)

#     label_12 = models.CharField(max_length=32, blank=True, null=True)
#     value_12 = models.CharField(max_length=32, blank=True, null=True)

#     label_13 = models.CharField(max_length=32, blank=True, null=True)
#     value_13 = models.CharField(max_length=32, blank=True, null=True)

#     label_14 = models.CharField(max_length=32, blank=True, null=True)
#     value_14 = models.CharField(max_length=32, blank=True, null=True)

#     label_15 = models.CharField(max_length=32, blank=True, null=True)
#     value_15 = models.CharField(max_length=32, blank=True, null=True)

#     label_16 = models.CharField(max_length=32, blank=True, null=True)
#     value_16 = models.CharField(max_length=32, blank=True, null=True)

#     label_17 = models.CharField(max_length=32, blank=True, null=True)
#     value_17 = models.CharField(max_length=32, blank=True, null=True)

#     label_18 = models.CharField(max_length=32, blank=True, null=True)
#     value_18 = models.CharField(max_length=32, blank=True, null=True)

#     label_19 = models.CharField(max_length=32, blank=True, null=True)
#     value_19 = models.CharField(max_length=32, blank=True, null=True)

#     label_20 = models.CharField(max_length=32, blank=True, null=True)
#     value_20 = models.CharField(max_length=32, blank=True, null=True)

#     label_21 = models.CharField(max_length=32, blank=True, null=True)
#     value_21 = models.CharField(max_length=32, blank=True, null=True)

#     label_22 = models.CharField(max_length=32, blank=True, null=True)
#     value_22 = models.CharField(max_length=32, blank=True, null=True)

#     label_22 = models.CharField(max_length=32, blank=True, null=True)
#     value_22 = models.CharField(max_length=32, blank=True, null=True)

#     label_23 = models.CharField(max_length=32, blank=True, null=True)
#     value_23 = models.CharField(max_length=32, blank=True, null=True)

#     label_24 = models.CharField(max_length=32, blank=True, null=True)
#     value_24 = models.CharField(max_length=32, blank=True, null=True)

#     label_25 = models.CharField(max_length=32, blank=True, null=True)
#     value_25 = models.CharField(max_length=32, blank=True, null=True)

#     label_26 = models.CharField(max_length=32, blank=True, null=True)
#     value_26 = models.CharField(max_length=32, blank=True, null=True)

#     label_27 = models.CharField(max_length=32, blank=True, null=True)
#     value_27 = models.CharField(max_length=32, blank=True, null=True)

#     label_28 = models.CharField(max_length=32, blank=True, null=True)
#     value_28 = models.CharField(max_length=32, blank=True, null=True)

#     label_29 = models.CharField(max_length=32, blank=True, null=True)
#     value_29 = models.CharField(max_length=32, blank=True, null=True)

#     label_30 = models.CharField(max_length=32, blank=True, null=True)
#     value_30 = models.CharField(max_length=32, blank=True, null=True)

#     label_31 = models.CharField(max_length=32, blank=True, null=True)
#     value_31 = models.CharField(max_length=32, blank=True, null=True)

#     label_32 = models.CharField(max_length=32, blank=True, null=True)
#     value_32 = models.CharField(max_length=32, blank=True, null=True)

#     label_33 = models.CharField(max_length=32, blank=True, null=True)
#     value_33 = models.CharField(max_length=32, blank=True, null=True)

#     label_34 = models.CharField(max_length=32, blank=True, null=True)
#     value_34 = models.CharField(max_length=32, blank=True, null=True)

#     label_35 = models.CharField(max_length=32, blank=True, null=True)
#     value_35 = models.CharField(max_length=32, blank=True, null=True)

#     label_36 = models.CharField(max_length=32, blank=True, null=True)
#     value_36 = models.CharField(max_length=32, blank=True, null=True)

#     label_37 = models.CharField(max_length=32, blank=True, null=True)
#     value_37 = models.CharField(max_length=32, blank=True, null=True)

#     label_38 = models.CharField(max_length=32, blank=True, null=True)
#     value_38 = models.CharField(max_length=32, blank=True, null=True)

#     label_39 = models.CharField(max_length=32, blank=True, null=True)
#     value_39 = models.CharField(max_length=32, blank=True, null=True)

#     label_40 = models.CharField(max_length=32, blank=True, null=True)
#     value_40 = models.CharField(max_length=32, blank=True, null=True)

#     label_41 = models.CharField(max_length=32, blank=True, null=True)
#     value_41 = models.CharField(max_length=32, blank=True, null=True)

#     label_42 = models.CharField(max_length=32, blank=True, null=True)
#     value_42 = models.CharField(max_length=32, blank=True, null=True)

#     label_43 = models.CharField(max_length=32, blank=True, null=True)
#     value_43 = models.CharField(max_length=32, blank=True, null=True)

#     label_44 = models.CharField(max_length=32, blank=True, null=True)
#     value_44 = models.CharField(max_length=32, blank=True, null=True)

#     label_45 = models.CharField(max_length=32, blank=True, null=True)
#     value_45 = models.CharField(max_length=32, blank=True, null=True)

#     label_46 = models.CharField(max_length=32, blank=True, null=True)
#     value_46 = models.CharField(max_length=32, blank=True, null=True)

#     label_47 = models.CharField(max_length=32, blank=True, null=True)
#     value_47 = models.CharField(max_length=32, blank=True, null=True)

#     label_48 = models.CharField(max_length=32, blank=True, null=True)
#     value_48 = models.CharField(max_length=32, blank=True, null=True)

#     label_49 = models.CharField(max_length=32, blank=True, null=True)
#     value_49 = models.CharField(max_length=32, blank=True, null=True)

#     label_50 = models.CharField(max_length=32, blank=True, null=True)
#     value_50 = models.CharField(max_length=32, blank=True, null=True)

#     def __str__(self):
#         return self.identifier
#     class Meta:
#         verbose_name="Tests"
#         verbose_name_plural="Tests"
    


