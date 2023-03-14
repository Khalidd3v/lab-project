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
    path("logout/", views.logoutuser, name="logout"),
    path("sub-manage-tests/", views.submanagetest , name="sub_manage_test"),
    path("select-test/", views.selecttest , name="select_test"),
    path("selected-tests/", views.selected_tests , name="selected_tests"),
    # path('Test-Result/', views.testresult, name='result'),
    

    path('upload/', views.upload_image, name='upload_image'),
    path('images/', views.my_images, name='my_images'),

  
    


    
]
