from django.http import request
from django.http.response import HttpResponseRedirect
from .models import user
from crud.forms import studentForm
from django.shortcuts import render
from django.contrib import messages
# Create your views here.
def index(request):
    if request.method =='POST':
        fm=studentForm(request.POST) 
        if fm.is_valid():
            name=fm.cleaned_data['name']
            email=fm.cleaned_data['email']
            password=fm.cleaned_data['password'] 
            mydata=user(name=name,email=email,password=password) 
            mydata.save() 
            messages.add_message(request, messages.SUCCESS, 'Your account create successfully') 

    else:
        fm=studentForm()
    stu=user.objects.all()
       
    return render(request, 'enroll/addandshow.html',{'form':fm,'data':stu})  

def delete(request,id):
    if request.method == 'POST':
        pi = user.objects.get(pk=id) 
        pi.delete()
        messages.error(request, 'Document deleted.') 
        return HttpResponseRedirect('/') 
        

def update(request,id):
    if request.method == 'POST':
        sm = user.objects.get(pk=id)
        fm = studentForm(request.POST, instance=sm) 
        if fm.is_valid():
            fm.save()
            return HttpResponseRedirect('/')
    
    else:
        pi = user.objects.get(pk=id)
        fm = studentForm( instance=pi)


    return render(request, 'enroll/update.html', {'form':fm}) 