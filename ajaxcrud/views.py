from django.http.response import JsonResponse
from django.shortcuts import render,HttpResponseRedirect
from .forms import studentform
from .models import student
from django.contrib import messages


# @csrf_exempt
def createandshow(request):
    if request.method=='POST':
        stud=studentform(request.POST)
        if stud.is_valid():
            # print('valid.........................................')
            myid=request.POST.get('id')
            nm=stud.cleaned_data['name']
            rl=stud.cleaned_data['roll']
            em=stud.cleaned_data['email']
            ps=stud.cleaned_data['password']
            if myid=='':
                # print('........ with out id.........')
                stud2=student(name=nm,roll=rl,email=em,password=ps)
            else:
                # print('........ with id.........')
                stud2=student(id=myid,name=nm,roll=rl,email=em,password=ps)

            stud2.save()
            # messages.success(request,'successfully saved record......')
            studdata=student.objects.values()
            studdata2=list(studdata)
            stud=studentform
            return JsonResponse({"status":"save","alldata":studdata2})

        else:
            # messages.error(request,'some data enered is incorrect.....')    
            return JsonResponse({"status":"sorry"})

    studdata=student.objects.values()
    studdata2=list(studdata)
    stud=studentform
    # return JsonResponse({'status':'save','alldata':studdata2})

    return render(request,'home.html',{'form':stud,'studdata':studdata})


def delete(request):
    if request.method=='POST':
        myid=request.POST.get('id')
        stdata=student.objects.get(id=myid)
        stdata.delete()
    # messages.success(request,'data deleted successfully........')
        return JsonResponse({'status':1})


def update(request):
    if request.method=='POST':
       myid=request.POST.get('id')
       stdata=student.objects.get(id=myid)
       stdata2={'roll':stdata.roll,'id':stdata.id,'name':stdata.name,'email':stdata.email,'password':stdata.password}
       return JsonResponse({'status':1,'studentdata':stdata2})