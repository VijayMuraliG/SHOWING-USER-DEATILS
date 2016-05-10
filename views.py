from django.shortcuts import render
from .models import Login,Signin


def index(request):
	return render(request,'index.html')

def form(request):
	return render(request,'form.html')

def form1(request):
	if request.method == 'POST':
		suname         = request.POST.get('uname')
        smnumber       = request.POST.get('mnumber')
        smailid        = request.POST.get('mailid')
        saddress       = request.POST.get('address')
        spassword      = request.POST.get('password')
        sconfirmpassword= request.POST.get('confirmpassword')
        q              = Signin(uname=suname,mnumber=smnumber,mailid=smailid,address=saddress,password=spassword,confirmpassword=sconfirmpassword)
        q.save()
       
        return render(request,'loginform.html') 

def form2(request):
	suname = request.POST.get('uname')
	spassword = request.POST.get('password')
	i=Signin.objects.get(uname=suname)
	i.id
	i.uname
	i.mnumber
	i.address
	i.mailid
	i.password
	return render(request,'details.html',{'uname':suname,'umnumber':i.mnumber,'uid':i.id,'mailid':i.mailid,'address':i.address,'password':i.password})
    
		
		













