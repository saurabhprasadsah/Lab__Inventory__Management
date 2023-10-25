from django import forms
from .models import *

class ChainOfCustody(forms.ModelForm):
    class Meta: #Meta will be represent the innner class Employeeform
        model =ChainOfCustody
        fields= ['Date','Client_ID','Order_of_the_Form','COC_File_Upload']
        widgets= {
            'Date':forms.TextInput(attrs={'class':'forms.control','placeholder':'Enter Date'}),
            'Client_ID':forms.TextInput(attrs={'class':'forms.control','placeholder':'Enter Client id'}),
            'Order_of_the_Form':forms.TextInput(attrs={'class':'forms.control','placeholder':'Enter order of the Number'}),
            'COC_File_Upload':forms.TextInput(attrs={'class':'forms.control','placeholder':'uploads files'}),
        }