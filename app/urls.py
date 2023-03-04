from django.urls import path
from .import views

urlpatterns = [

    path("", views.home, name="home"),
    path("add-patient/", views.add_patient, name="add_patient"),
    path("add-doctor/", views.add_doctor, name="add_doctor"),
    path("manage-patient/", views.manage_patient, name="manage_patient"),
    path("delete/<str:pk>/", views.deleteit, name="delete"),
    path("update/<str:pk>/", views.updatepatient, name="update"),
    path("login", views.loginuser, name="login"),
    
]
