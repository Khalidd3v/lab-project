from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth import login, logout, authenticate
from .forms import *
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import *
from django.http import JsonResponse



@login_required
def home(request):
    return render(request, 'app/home.html')



@login_required
def add_patient(request):
    if request.method == 'POST':
        form = RegisterPatientForm(request.POST)
        if form.is_valid():
            # Save patient and store patient ID in session
            patient = form.save()
            request.session['patient_id'] = patient.pk
            return redirect('select_test')
    else:
        form = RegisterPatientForm()
    return render(request, 'app/add_patient.html', {'form': form})


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


@login_required
def submanagetest(request):
    return render(request, 'app/sub_manage_tests.html')

@login_required
def upload_image(request):
    if request.method == 'POST':
        img = request.FILES['image']
        images = MyImage(image = img, caption="nohting")
        images.save()

    return render(request, 'app/img.html')

@login_required
def my_images(request):
    images = MyImage.objects.all()
    return render(request, 'app/show_img.html', {'images': images})


@login_required
def selecttest(request):
    # Retrieve patient ID from session
    patient_id = request.session.get('patient_id')
    if patient_id is None:
        return redirect('add_patient')
    if request.method == 'POST':
        form = TestSelectionForm(request.POST)
        if form.is_valid():
            # Store selected test names and patient ID in session
            request.session['selected_tests'] = form.cleaned_data['tests']
            request.session['patient_id'] = patient_id
            return redirect('selected_tests')
    else:
        form = TestSelectionForm()
    return render(request, 'app/select_tests.html', {'form': form})

@login_required
def selected_tests(request):
    # Retrieve selected test names and patient ID from session
    selected_tests = request.session.get('selected_tests', [])
    patient_id = request.session.get('patient_id')
    if patient_id is None:
        return redirect('register_patient')
    # Create modelforms for selected tests
    test1_form = CBCTestForm(request.POST or None, prefix='CBC Test') if 'CBC Test' in selected_tests else None
    test2_form = BioChemistryTestForm(request.POST or None, prefix='Bio Chemistry Test') if 'Bio Chemistry Test' in selected_tests else None
    test3_form = StoolRETestForm(request.POST or None, prefix='Stool RE Test') if 'Stool RE Test' in selected_tests else None
    test4_form = UrineRETestForm(request.POST or None, prefix='Urine RE Test') if 'Urine RE Test' in selected_tests else None
    test5_form = SerologyTestForm(request.POST or None, prefix='Serology Test') if 'Serology Test' in selected_tests else None
    test6_form = SemenTestForm(request.POST or None, prefix='Semen Test') if 'Semen Test' in selected_tests else None
    test7_form = CRPTestForm(request.POST or None, prefix='CRP Test') if 'CRP Test' in selected_tests else None
    test8_form = ThyroidTestForm(request.POST or None, prefix='Thyroid Test') if 'Thyroid Test' in selected_tests else None
    test9_form = KedneyFunctionTestForm(request.POST or None, prefix='Kedney Function Test') if 'Kedney Function Test' in selected_tests else None
    test10_form = LiverFunctionTestForm(request.POST or None, prefix='Liver Function Test') if 'Liver Function Test' in selected_tests else None
    test11_form = GlucoseBFTestForm(request.POST or None, prefix='Glucose BF Test') if 'Glucose BF Test' in selected_tests else None
    if request.method == 'POST':
        # Save modelforms for selected tests with patient ID
        if test1_form is not None and test1_form.is_valid():
            test1 = test1_form.save(commit=False)
            test1.patient_id = patient_id
            test1.save()
        if test2_form is not None and test2_form.is_valid():
            test2 = test2_form.save(commit=False)
            test2.patient_id = patient_id
            test2.save()
        if test3_form is not None and test3_form.is_valid():
            test3 = test3_form.save(commit=False)
            test3.patient_id = patient_id
            test3.save()
        if test4_form is not None and test4_form.is_valid():
            test4 = test4_form.save(commit=False)
            test4.patient_id = patient_id
            test4.save()
        if test5_form is not None and test5_form.is_valid():
            test5 = test5_form.save(commit=False)
            test5.patient_id = patient_id
            test5.save()
        if test6_form is not None and test6_form.is_valid():
            test6 = test6_form.save(commit=False)
            test6.patient_id = patient_id
            test6.save()
        if test7_form is not None and test7_form.is_valid():
            test7 = test7_form.save(commit=False)
            test7.patient_id = patient_id
            test7.save()
        if test8_form is not None and test8_form.is_valid():
            test8 = test8_form.save(commit=False)
            test8.patient_id = patient_id
            test8.save()
        if test9_form is not None and test9_form.is_valid():
            test9 = test9_form.save(commit=False)
            test9.patient_id = patient_id
            test9.save()
        if test10_form is not None and test10_form.is_valid():
            test10 = test10_form.save(commit=False)
            test10.patient_id = patient_id
            test10.save()
        if test11_form is not None and test11_form.is_valid():
            test11 = test11_form.save(commit=False)
            test11.patient_id = patient_id
            test11.save()
        return redirect('result', pk=patient_id)
    return render(request, 'app/selected_tests.html', 
                            {'test1_form': test1_form,
                             'test2_form': test2_form, 'test3_form': test3_form,
                                'test4_form': test4_form, 'test5_form': test5_form,
                                    'test6_form': test6_form, 'test7_form': test7_form,
                                       'test8_form': test8_form, 'test9_form': test9_form,
                                          'test10_form': test10_form, 'test11_form': test11_form,
                                        })



@login_required
def testresult(request, pk):

    # Get the patient object with the given ID
    patient = Patient.objects.get(pk=pk)

    # Get all the CBC tests related to this patient
    cbc_tests = patient.cbc_tests.all()

    # Get all the biochemistry tests related to this patient
    biochemistry_tests = patient.bio_chemistry_tests.all()

    # Get all the stool r/e tests related to this patient
    stoolre_tests = patient.stoolre_tests.all()

    # Get all the urine r/e tests related to this patient
    urine_tests = patient.urine_tests.all()

    # Get all the serology tests related to this patient
    serology_tests = patient.serology_tests.all()

     # Get all the semen tests related to this patient
    semen_tests = patient.semen_tests.all()

    # Get all the crps tests related to this patient
    crp_tests = patient.crp_tests.all()

    # Get all the stool r/e tests related to this patient
    thyroid_tests = patient.thyroid_tests.all()

    # Get all the kedney function tests related to this patient
    kedney_function_tests = patient.kedney_function_tests.all()

    # Get all the liver funtion tests related to this patient
    liver_function_tests = patient.liver_function_tests.all()

    # Get all the glucose bf tests related to this patient
    glucose_bf_tests = patient.glucose_bf_tests.all()


    
    return render(request, 'app/generate_result.html', 
                  {'patient': patient, 'cbc_tests': cbc_tests,
                    'biochemistry_tests': biochemistry_tests, 'stoolre_tests': stoolre_tests,
                        'urine_tests':urine_tests,'serology_tests':serology_tests,'semen_tests':semen_tests,
                            'crp_tests':crp_tests, 'thyroid_tests':thyroid_tests, 'kedney_function_tests':kedney_function_tests,
                                'liver_function_tests':liver_function_tests, 'glucose_bf_tests':glucose_bf_tests,})



#all patient management Code
@login_required
def patientapi(request):
    patients = Patient.objects.all().values()
    return JsonResponse({'patients': list(patients)})





    