from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth import login, logout, authenticate
from .forms import *
from django.contrib import messages
from django.contrib.auth.decorators import login_required


@login_required
def home(request):
    return render(request, 'app/home.html')



@login_required
def add_patient(request):
    if request.method == "POST":
        form = RegisterPatientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = RegisterPatientForm()

    return render(request, 'app/add_patient.html', {"form":form})


@login_required
def add_doctor(request):
    if request.method == "POST":
        form = RegisterDoctorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = RegisterDoctorForm()
    return render(request, 'app/add_doctor.html', {"form":form})

@login_required
def manage_patient(request):
    patients = Patient.objects.all()
    context = {
        "patients": patients
    }
    return render(request, 'app/manage_patient.html', context)



@login_required
def deleteit(request, pk):
    deletedata = get_object_or_404(Patient, id=pk)
    deletedata.delete()
    return redirect('manage_patient')



@login_required
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

    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
   
        else:
            messages.error(request, "Username or Password is Incorrect !!! ")
            return redirect('login')
        
        
    return render(request, 'app/login.html')

def logoutuser(request):
    logout(request)
    return redirect('login')