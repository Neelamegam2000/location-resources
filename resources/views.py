from django.shortcuts import render 
from django.conf import settings
from resources.forms import resourcesForm
from .models import resources   
from django.db.models import Q
work1="" 
pincode1=""
def home(request):  
	if(request.method=="POST"):
	    form=resourcesForm(request.POST) 
	    form.save()  
	    res=resources()
	    res.name=form.cleaned_data['name'] 
	    res.location=form.cleaned_data['location'] 
	    res.address=form.cleaned_data['address'] 
	    res.pincode=form.cleaned_data['pincode'] 
	    res.email=form.cleaned_data['email'] 
	    res.work=form.cleaned_data['work'] 
	    res.phone_number=form.cleaned_data['phone_number']  
	    #t=resources.objects.last() 
	    #id1=resources.objects.values_list('name').count()+1 
	    #t.identifier=id1 
	    #t.save()
	return render(request,'resources.html',{'form':resourcesForm()})
def user(request): 
	if(request.method=="POST"): 
		global work1
		global pincode1
		global alldata
		work1=request.POST.get('work')
		pincode1=request.POST.get('pincode')
		print(work1,pincode1)
		alldata=resources.objects.filter(work=request.POST.get('work'))|resources.objects.filter(pincode=request.POST.get('pincode'))  
		return render(request,'details.html',{'alldata':alldata})
	return render(request,'user.html',) 
def direction(request):  
	if(request.method=="POST"):
		dirdata=resources.objects.values('location').filter(Q(id=request.POST.get('identifier'))&((Q(work=work1))|(Q(pincode=pincode1))))
		print(dirdata)
		lat=dirdata[0]['location'][0]
		lon=dirdata[0]['location'][1]
		print(lat,lon)
	return render(request,'direction.html',{'lat':lat,'lon':lon})
   
