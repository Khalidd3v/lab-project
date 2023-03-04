from django.contrib import admin
from .models import *


MyAllModels = (Patient, Doctor, CBCTest, BioChemistryTest, 
               StoolRETest, UrineReTest, SerologyTest, SemenTest,
               CRPTest, ThyroidTest, KedneyFunctionTest, LiverFunctionTest,
               )

for m in MyAllModels:
    admin.site.register(m)
