from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Region_code(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    pincode=models.CharField(max_length=50,blank=True,null=True)
    date=models.DateTimeField(auto_now=True,blank=True,null=True)
    class Meta:
        db_table="region code"
class Items(models.Model):
    admin=models.ForeignKey(User,on_delete=models.CASCADE)
    name=models.CharField(max_length=255,blank=True,null=True)
    date=models.DateTimeField(auto_now=True)
    class Meta:
        db_table="items"
class Vender(models.Model):
    admin=models.ForeignKey(User,related_name="user", on_delete=models.CASCADE)
    first_name=models.CharField(max_length=150,blank=True,null=True)
    last_name=models.CharField(max_length=150,blank=True,null=True)
    phone=models.CharField(max_length=15,blank=True,null=True)
    adders=models.TextField(blank=True,null=True)
    date=models.DateTimeField(auto_now=True,blank=True,null=True)
    region_code=models.ForeignKey(Region_code, on_delete=models.CASCADE)
    item=models.ForeignKey(Items,on_delete=models.CASCADE)
    class Meta:
        db_table="vender"

class Vender_review(models.Model):
    vender=models.ForeignKey(Vender,  on_delete=models.CASCADE)
    evaluator=models.ForeignKey(User,  on_delete=models.CASCADE)
    rating=models.FloatField(blank=True,null=True)
    comments=models.TextField(blank=True,null=True)
    feedback=models.TextField(blank=True,null=True)
    post_date=models.DateTimeField(auto_now=True)
    class Meta:
        db_table="vender review"
    