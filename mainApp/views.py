from django.shortcuts import render,HttpResponseRedirect
from .models import *
from django.core.paginator import Paginator
from django.db.models import Q


def Login(Request):
    return render(Request,"Login.html")

def homePage(Request):
    return render(Request,"home.html")

def chain_of_custody(Request):
    data = ChainOfCustody.objects.all()
    data = ChainOfCustody.objects.all().order_by("id")
    paginator = Paginator(data, 10)
    page_number = Request.GET.get("page")
    page_obj = paginator.get_page(page_number) 
    return render(Request,"Chain of Custody.html",{'data':page_obj})



def editrecord(Request,id):
    try:    
        data = ChainOfCustody.objects.get(id=id)
        if(Request.method == "POST"):
            data.Date =  Request.POST.get("Date")
            data.Client_ID =  Request.POST.get("Client_ID")
            data.Order_of_the_Form =  Request.POST.get("Order_of_the_Form")
            data.COC_File_Upload =  Request.POST.get("COC_File_Upload")
            data.save()
            return render(Request,"Chain of Custody.html")
        return render(Request,"editfrom.html",{'data':data}) 
    except:
        return render(Request ,"Chain of Custody.html")

 

def chain_of_custody_form(Request):
    if(Request.method =="POST"):
        c = ChainOfCustody()
        c.Date =  Request.POST.get("Date")
        c.Client_ID =  Request.POST.get("Client_ID")
        c.Order_of_the_Form =  Request.POST.get("Order_of_the_Form")
        myfile =  Request.FILES.getlist("COC_File_Upload")
        for f in myfile:
            ChainOfCustody(COC_File_Upload=f)
            c.save()
        return render(Request,'Chain of Custody.html')    
    return render(Request, 'Chain of Custody Form.html')




def SampleIntakelog(Request):
    data = SampleIntakeForm.objects.all()
    data = SampleIntakeForm.objects.all().order_by("id")
    paginator = Paginator(data, 1)
    page_number = Request.GET.get("page")
    page_obj = paginator.get_page(page_number) 
    return render(Request, "Sample Intake log.html",{'data':page_obj})



# def searchPage(Request):
#     if(Request.method=="POST"):
#         search = Request.POST.get('search')
#         data = ChainOfCustody.objects.filter(Q(Date__icontains=search)|Q(Client_ID__icontains=search))
#         return render(Request,"Sample Intake log.html",{'data':data})
#     else:
#         return HttpResponseRedirect("/")


def Sample_Intake_Form(Request):
     if(Request.method=="POST"):
        s = SampleIntakeForm()
        s.Date =  Request.POST.get("Date")
        s.Sample_ID =  Request.POST.get("Sample_ID")
        s.Sample_Name =  Request.POST.get("Sample_Name")
        s.Matrix =  Request.POST.get("Matrix")
        s.Batch_Number =  Request.POST.get("Batch_Number")
        s.Sample_Size =  Request.POST.get("Sample_Size")
        s.Batch_Size =  Request.POST.get("Batch_Size")
        s.Distributor_Micro_business_Name =  Request.POST.get("Distributor_Micro_business_Name")
        s.Distributor_Micro_business_License_No =  Request.POST.get("Distributor_Micro_business_License_No")
        s.Chain_of_Custody_Number =  Request.POST.get("Chain_of_Custody_Number")
        s.save()
        return render(Request, "Sample Intake log.html")
     return render(Request,"Sample Intake Form.html")


def editsampleform(Request,id):
    try:    
        data = SampleIntakeForm.objects.get(id=id)
        if(Request.method=="POST"):
            s = SampleIntakeForm()
            s.Date =  Request.POST.get("Date")
            s.Sample_ID =  Request.POST.get("Sample_ID")
            s.Sample_Name =  Request.POST.get("Sample_Name")
            s.Matrix =  Request.POST.get("Matrix")
            s.Batch_Number =  Request.POST.get("Batch_Number")
            s.Sample_Size =  Request.POST.get("Sample_Size")
            s.Batch_Size =  Request.POST.get("Batch_Size")
            s.Distributor_Micro_business_Name =  Request.POST.get("Distributor_Micro_business_Name")
            s.Distributor_Micro_business_License_No =  Request.POST.get("Distributor_Micro_business_License_No")
            s.Chain_of_Custody_Number =  Request.POST.get("Chain_of_Custody_Number")
            s.save()
            return render(Request, "Sample Intake log.html")
        else:     
            return render(Request, "Editsampleintakeform.html",{'data':data})
    except:
        return render(Request, "Sample Intake log.html")















def SampleTrackingLog(Request):
    return render(Request,"Sample Tracking Log.html")

def SampleTrackingForm(Request):
    return render(Request,"Sample Tracking Form.html")

def SampleRetainLog(Request):
    return render(Request,"Sample Retention Log.html")

def SampleRetainForm(Request):
    return render(Request,"Sample Retention Form.html")