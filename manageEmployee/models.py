from django.db import models

class Employee(models.Model):
    empID = models.BigAutoField(primary_key=True)
    Name = models.CharField(max_length=10)
    Age = models.IntegerField()
    class Meta:
        db_table = "EMPLOYEES"
    
class Product(models.Model):
    productId = models.BigAutoField(primary_key=True)
    productName = models.CharField(max_length=25)
    eID = models.ForeignKey(Employee,on_delete=models.CASCADE,db_column="eID")
    class Meta:
        db_table="PRODUCTS"