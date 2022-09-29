from django.shortcuts import render 
from django.conf import settings
from resources.forms import resourcesForm, statusForm
from .models import resources,status
from .models import login 
from django.db.models import Q
from django.core.mail import send_mail, EmailMessage
import random
def login1(request):
	msg=""
	otp_check=""
	if(request.method=="POST"):
		if("sign_up" in request.POST):
			global otp
			global name
			global password
			global email
			if((request.POST.get('password'))==(request.POST.get('con_password'))):
			    num=['0','1','2','3','4','5','6','7','8','9']
			    otp=""
			    name=request.POST.get('name')
			    email=request.POST.get('email')
			    password=request.POST.get('password')
			    for i in range(0,8):
				    otp=otp+random.choice(num)
			    subject="Location resources verification email"
			    msg="your OTP is "+otp
			    email_from=settings.EMAIL_HOST_USER
			    recipient=[request.POST.get('email'),]
			    mail=EmailMessage(subject,msg,email_from,recipient)
			    mail.send()
			    print(otp,name,password,email)
			    return render(request,"verifyer.html",)
			else:
				return render(request,"login1.html",)
		elif("verify" in request.POST):
			if(otp==request.POST.get('otp')):
				log=login()
				log.name=name
				log.email=email
				log.password=password
				log.save()
				otp_check="**successfully signed up"
				return render(request,"login1.html",{'otp_check':otp_check})
			else:
				otp_check="**you entered OTP is wrong"
				return render(request,"verifyer.html",{'otp_check':otp_check})
	if(request.method=="GET"):
		if("sign_in" in request.GET):
			global email2
			global alldata
			email2=request.GET.get('email')
			userdata=login.objects.filter(Q(email=request.GET.get('email'))&Q(password=request.GET.get('password'))).count()
			if(userdata>0):
				alldata=resources.objects.filter(email=request.GET.get('email'))
				print(alldata)
				return render(request,"ownerdetails.html",{'alldata':alldata,'email2':email2,'statusdata':statusForm(),'existingstatus':status.objects.all()})
			else:
				if(email2!=""):
					msg="**You entered email and password is wrong"
					return render(request,"login1.html",{'msg':msg})
				else:
					return render(request,"login1.html",)			
	return render(request,"login1.html",)
def home(request):  
	if(request.method=="POST"):
		form=resourcesForm(request.POST,request.FILES or None)
		print(form)
		form.save()  
	     
	    #t=resources.objects.last() 
	    #id1=resources.objects.values_list('name').count()+1 
	    #t.identifier=id1 
	    #t.save()
		return render(request,'ownerdetails.html',{'alldata':resources.objects.filter(email=form.cleaned_data['email']),'statusdata':statusForm(),'existingstatus':status.objects.all()})
	return render(request,'resources.html',{'form':resourcesForm()})
def details(request): 
	if(request.method=="GET"): 
		global work1
		global pincode1
		global alldata
		work1=request.GET.get('work')
		pincode1=request.GET.get('pincode')
		print(work1,pincode1)
		alldata=resources.objects.filter(work=request.GET.get('work'))&resources.objects.filter(pincode=request.GET.get('pincode'))  
	return render(request,'details.html',{'alldata':alldata,'existingstatus':status.objects.all()})
def user(request):		
	return render(request,'user.html') 
def direction(request): 
	global id1
	if(request.method=="GET"):
		id1=request.GET.get('reg_id')
		print(id1)
		dirdata=resources.objects.values('location').filter(Q(id=request.GET.get('reg_id'))&((Q(work=work1))|(Q(pincode=pincode1))))
		lat=dirdata[0]['location'][0]
		lon=dirdata[0]['location'][1] 
	return render(request,'direction.html',{'lat':lat,'lon':lon})

#from django.views.decorators.cache import cache_control
#@cache_control(no_cache=True, must_revalidate=True)
def editdetails(request):
	msg=""
	global id2
	if("edit" in request.POST and request.method=="POST"):
		id2=request.POST.get('identifier')
		myreqdata=resources.objects.get(Q(id=id2)&Q(email=email2))
		form=resourcesForm(instance=myreqdata)
		print(myreqdata)
		if(resources.objects.filter(Q(id=id2)&Q(email=email2)).count()>0):
			return render(request,"editdetails.html",{'form':form})
		else:
			msg="**Please enter the valid id"
			print(msg)
			return render(request,"ownerdetails.html",{'alldata':alldata,'msg':msg})
	if(request.method=="GET"):
		id2=request.GET.get('identifier')
		myreqdata=resources.objects.get(Q(id=id2)&Q(email=email2))
		form=resourcesForm(instance=myreqdata)
		print(myreqdata)
		if(resources.objects.filter(Q(id=id2)&Q(email=email2)).count()>0):
			return render(request,"editdetails.html",{'form':form})
		else:
			return render(request,"ownerdetails.html",{'alldata':alldata})
					
	if("delete" in request.POST and request.method=="POST"):
		id2=request.POST.get('identifier')
		myreqdata=resources.objects.filter(Q(id=id2)&Q(email=email2))
		if(myreqdata.count()>0):
			resources.objects.filter(Q(id=id2)&Q(email=email2)).delete()
			return render(request,"ownerdetails.html",{'alldata':resources.objects.filter(email=email2)})
		else:
			msg="**Plese enter the valid id"
			return render(request,"ownerdetails.html",{'alldata':alldata,'msg':msg})
	if('submit1' in request.POST):
		myreqdata=resources.objects.get(Q(id=id2)&Q(email=email2))
		form=resourcesForm(request.POST or None,request.FILES or None,instance=myreqdata)
		if(form.is_valid()):
			form.save()
			mystatusdata=status.objects.values('status').filter(resources_id=resources.objects.get(id=id2))
			#edit=resources.objects.filter(id=id2).update(name=form.cleaned_data['name'],location=form.cleaned_data['location'],address=form.cleaned_data['address'],pincode=form.cleaned_data['pincode'],phone_number=form.cleaned_data['phone_number'],work=form.cleaned_data['work'],email=form.cleaned_data['email'],profile_picture=request)
			return render(request,"ownerdetails.html",{'alldata':resources.objects.filter(email=email2),'statusdata':statusForm(),'existingstatus':status.objects.all()})
	if("logout" in request.POST):
		return render(request,"login1.html",)
	return render(request,"editdetails.html",)
def review(request):
	if(request.method=="POST"):
		comments=request.POST.get('comments')
		if(comments!=""):
			print(comments)
			already_review=resources.objects.values('review').filter(id=id1)
			q=already_review[0]['review']
			if(len(q)==0):
				comments1=comments
			else:
				comments1=q+","+comments
			print(comments1)
			t=resources.objects.filter(id=id1).update(review=comments1)
			print(t)
	return render(request,"review.html")
def forgetpass(request):
	msg=""
	print(1)
	if(request.method=="POST"):
		global email1
		global otp1
		if('verify' in request.POST):
			print(otp1,request.POST.get('otp'))
			if(otp1==request.POST.get('otp')):
				return render(request,"new_password.html",)
			else:
				return render(request,"verifyer.html",)
		elif("change" in request.POST):
			if(request.POST.get('password')!="" and request.POST.get("confirm_password")!="" ):
				login.objects.filter(email=email1).update(password=request.POST.get('password'))
				return render(request,"login1.html",)
			else:
				return render(request,"new_password.html",)
		else:
			email1=request.POST.get('email')
			num_list1=['0','1','2','3','4','5','6','7','8','9']
			otp1=""
			for i in range(0,5):
				otp1=otp1+random.choice(num_list1)
			subject="Forget password"
			mail_from=settings.EMAIL_HOST_USER
			recipient=[email1,]
			messages="Your OTP is "+otp1
			mail=EmailMessage(subject,messages,mail_from,recipient)
			mail.send()
			return render(request,"verifyer.html",)
	return render(request,"email_pass.html",)
def resourcestatus(request):
	global statusid
	if(request.method=="POST"):
		statusid=request.POST.get("id")
		form = statusForm(request.POST)
		existingresources=resources.objects.get(id=statusid)
		existingstatus=status.objects.filter(resources_id=existingresources)
		if(form.is_valid and existingstatus.count()==0):
			print(form)
			form1=status.objects.create(resources_id=existingresources,status=form.cleaned_data['status'])
			return render(request,"ownerdetails.html",{'alldata':resources.objects.filter(email=email2),'statusdata':statusForm(),'existingstatus':status.objects.all()})
		elif(form.is_valid() and existingstatus.count()>0):
			form2=status.objects.filter(resources_id=existingresources).update(status=form.cleaned_data['status'])
			return render(request,"ownerdetails.html",{'alldata':resources.objects.filter(email=email2),'statusdata':statusForm(),'existingstatus':status.objects.all()})

			
			

	

   
