from django.db import models

# Create your models here.

class AccountCreationDetails(models.Model):
    UserId = models.AutoField(primary_key=True)
    NameOfOrgranization = models.CharField(
        max_length=500, null=False, blank=False)
    EmailID = models.EmailField(
        max_length=200, unique=True, null=False, blank=False)
    Address = models.CharField(max_length=300, null=False, blank=False)
    GST = models.CharField(max_length=20,blank=True)
    AuthorisedSignatoryName = models.CharField(max_length=100)
    ContactNumber = models.CharField(max_length=10)
    BusinessType = models.CharField(max_length=100)
    Password=models.CharField(max_length=13,null=False)


    class Meta:
        ordering = ['-UserId']


class ProductDetails(models.Model):
    product_id = models.AutoField(primary_key=True)
    UserId = models.ForeignKey(AccountCreationDetails, on_delete=models.CASCADE)
    machine_type = models.CharField(max_length=100)
    name_of_machine = models.CharField(max_length=100)
    machine_manufacturer = models.CharField(max_length=100)
    machine_model_number = models.CharField(max_length=100)
    machine_build_date = models.DateField()
    machine_condition = models.CharField(max_length=100)
    machine_dimension = models.CharField(max_length=100)
    machine_weight = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    selling_price = models.DecimalField(max_digits=10, decimal_places=2)
    location_of_machine = models.CharField(max_length=100)
    machine_image_1 = models.ImageField(upload_to='media/')
    machine_image_2 = models.ImageField(upload_to='media/',blank=True)
    machine_image_3 = models.ImageField(upload_to='media/',blank=True)
    machine_image_4 = models.ImageField(upload_to='media/',blank=True)

    class Meta:
        ordering = ['-product_id']