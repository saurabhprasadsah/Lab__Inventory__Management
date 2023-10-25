from django.urls import path
from .views import *
from . import views

app_name= "mainapp"

urlpatterns = [
    path('',Login),
    path("upload",chain_of_custody_form, name="uploads"),
    path('homepage/', homePage),
    path('chain_of_custody/', chain_of_custody),
    path('chain_of_custody_form/', chain_of_custody_form),


    path('edit/<int:id>/', editrecord),
    path('SampleIntakelog/', SampleIntakelog),
    path('editsampleform/<int:id>/',editsampleform),
    path('Sample_Intake_Form/', Sample_Intake_Form),

    
    path('SampleTrackingLog/', SampleTrackingLog),
    path('SampletrackingForm/', SampletrackingForm),
    path('SampleRetainLog/', SampleRetainLog),
    path('SampleRetainForm/', SampleRetainForm),       
]
app_name = 'labs'