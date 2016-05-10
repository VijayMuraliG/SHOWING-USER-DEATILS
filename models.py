from django.db import models

class Signin(models.Model):
	uname=models.CharField(max_length=200)
	mnumber=models.CharField(max_length=200)
	mailid=models.CharField(max_length=200)
	address=models.CharField(max_length=200)
	password=models.IntegerField()
	confirmpassword=models.IntegerField()

	def vijay(self):
		return "%s - %s -%s" %(self.uname,self.address,self.password)


class Login(models.Model):
	uname=models.CharField(max_length=200)
	password=models.IntegerField()
	

