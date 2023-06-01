from django.db import models

class Customer(models.Model):
   first_name=models.CharField(max_length=15,null=True,blank=True)
   last_name=models.CharField(max_length=15,null=True,blank=True)
   mobile_number=models.IntegerField(null=True,blank=True)
   address=models.TextField(null=True,blank=True)
   age=models.IntegerField(null=True,blank=True)
   country_name=models.CharField(max_length=20,null=True,blank=True) 
   DOB=models.DateField(max_length=20,null=True,blank=True)

   def __str__(self):
      return str(self.first_name)
class CustomerAddress(models.Model):
   Customer=models.ForeignKey(Customer,on_delete=models.CASCADE,null=True,related_name='customer_addresses')
   street_name=models.CharField(max_length=15,null=True,blank=True)
   street_no=models.IntegerField(null=True,blank=True)
   city=models.CharField(max_length=15,null=True,blank=True)
   state=models.CharField(max_length=15,null=True,blank=True)
   country=models.CharField(max_length=15,null=True,blank=True)
   pincode=models.IntegerField(null=True,blank=True)

   
   def __str__(self):
      return str(self.street_name)
   

class CustomerAdhar(models.Model):
   Customer=models.OneToOneField(Customer,on_delete=models.CASCADE)
   adhar_no=models.IntegerField(null=True,blank=True)
   father_name=models.CharField(max_length=15,null=True,blank=True)
   gender=models.CharField(max_length=15,null=True,blank=True)
   dob=models.IntegerField(null=True,blank=True)

   def __str__(self):
      return str(self.adhar_no)