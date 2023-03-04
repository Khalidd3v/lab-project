from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .forms import *


def home(request):
    return render(request, 'app/home.html')




def add_patient(request):
    if request.method == "POST":
        form = RegisterPatientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = RegisterPatientForm()

    return render(request, 'app/add_patient.html', {"form":form})

def add_doctor(request):
    if request.method == "POST":
        form = RegisterDoctorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = RegisterDoctorForm()
    return render(request, 'app/add_doctor.html', {"form":form})


def manage_patient(request):
    patients = Patient.objects.all()
    context = {
        "patients": patients
    }
    return render(request, 'app/manage_patient.html', context)

def deleteit(request, pk):
    deletedata = get_object_or_404(Patient, id=pk)
    deletedata.delete()
    return redirect('manage_patient')

def updatepatient(request, pk):
    patient = get_object_or_404(Patient, id=pk )

    if request.method == "POST":
        form = RegisterPatientForm(request.POST, instance=patient)
        if form.is_valid():
            form.save()
            return redirect('manage_patient')
    else:
        form = RegisterPatientForm(instance=patient)
    context = {
        "form":form,
        "pk":pk
    }
    
    return render(request, 'app/add_patient.html', context)



def loginuser(request):
    return render(request, 'app/login.html')