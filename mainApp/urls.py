from django.urls import path
from .views import *
from . import views

app_name= "mainapp"

urlpatterns = [
    path('',Login),
    path("upload",chain_of_custody_form, name="uploads"),
    path('homepage/', homePage),
    path('chain_of_custody/', chain_of_custody, ),
    path('chain_of_custody_form/', chain_of_custody_form),
    path('edit/<int:id>/', editrecord),
    path('SampleIntakelog/', SampleIntakelog),

    # path('searchPage/',searchPage,name="search"),

    path('Sample_Intake_Form/', Sample_Intake_Form),
    
    path('SampleTrackingLog/', SampleTrackingLog),
    path('SampleTrackingForm/', SampleTrackingForm),
    path('SampleRetainLog/', SampleRetainLog),
    path('SampleRetainForm/', SampleRetainForm),    
    
]

app_name = 'labs'