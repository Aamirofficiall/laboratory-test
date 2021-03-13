from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import render,redirect
from .forms import *
from .models import *

@login_required(login_url='login')
def report(request):
    return render(request,'report.html')

@login_required(login_url='login')
def createReport(request):
    form=TestReportForm()
    
    if request.method ==  'POST':
        form=TestReportForm(request.POST)
       
        patientName=request.POST.get('patientName')
        raterName=request.POST.get('raterName')
        date_created=request.POST.get('date_created')
        obj = TestReport.objects.create(
            patientName=patientName,raterName=raterName,date_created=date_created,
            user=request.user
            )
        obj.save()
        messages.success(request, 'Report created successfully') 
        return redirect('create-test',id=obj.id)

    return render(request,'createReport.html',{'form':form})

@login_required(login_url='login')
def createTest(request,id):
    obj = TestReport.objects.get(id=id)

    if request.method =='POST':
        grasp=0
        grasp1 = int(request.POST.get('grasp1'))
        grasp2 = int(request.POST.get('grasp2'))
        grasp3 = int(request.POST.get('grasp3'))
        grasp4 = int(request.POST.get('grasp4'))
        grasp5 = int(request.POST.get('grasp6'))
        grasp6 = int(request.POST.get('grasp5'))
        grasp = grasp1 + grasp2 + grasp3 + grasp4 + grasp5 + grasp6

        grip=0
        grip1 = int(request.POST.get('grip1'))
        grip2 = int(request.POST.get('grip2'))
        grip = grip1 + grip2      

        pinch=0
        pinch1 = int(request.POST.get('pinch1'))
        pinch2 = int(request.POST.get('pinch2'))
        pinch3 = int(request.POST.get('pinch3'))
        pinch4 = int(request.POST.get('pinch4'))
        pinch5 = int(request.POST.get('pinch6'))
        pinch6 = int(request.POST.get('pinch5'))
        pinch = pinch1 + pinch2 + pinch3 + pinch4 + pinch5 + pinch6

        gross=0
        gross1 = int(request.POST.get('gross1'))
        gross2 = int(request.POST.get('gross2'))
        gross3 = int(request.POST.get('gross3'))
        gross4 = int(request.POST.get('gross4'))        
        gross = gross1 + gross2 + gross3 + gross4

        obj = TestReport.objects.get(id=id)
        obj.grasp_score = grasp
        obj.grip_score = grip
        obj.pinch_score = pinch
        obj.gross_score = gross
        obj.save()

        return redirect('complete-test-results',id=obj.id)


    
    return render(request,'createTest.html',{'obj':obj})


@login_required(login_url='login')
def completeTestResults(request,id): 
    obj = TestReport.objects.get(id=id)
    return render(request,'results.html',{'obj':obj})


@login_required(login_url='login')
def testResultsList(request): 
    objects = TestReport.objects.all()
    return render(request,'testResultsList.html',{'objects':objects})





