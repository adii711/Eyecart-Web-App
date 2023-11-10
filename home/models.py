from django.db import models
from django.contrib.auth.models import User
# Create your models here.
# models.py
class YourModel(models.Model):
    title = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2,default=0)
    image = models.ImageField(upload_to='images/')
    def __str__(self):
        return self.title

class CartItem(models.Model):
    product = models.ForeignKey(YourModel, on_delete=models.CASCADE)
    # img = models.ForeignKey(YourModel,on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=0)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date_added = models.DateTimeField(auto_now_add=True)
 
    def __str__(self):
        return f'{self.quantity} x {self.product.name}'
    

class newform(models.Model):
    firstname = models.CharField(max_length=50, blank=False, null=False, primary_key=True)
    lastname = models.CharField(max_length=50, blank=False, null=False)
    password = models.CharField(max_length=50, blank=False, null=False)
    age = models.IntegerField(blank=False, null=False)
    email = models.EmailField(blank=False, null=False)
    address = models.TextField(blank=False, null=False)
    phoneno = models.IntegerField(blank=False, null=False)
    genders = [('M', 'MALE'), ('F', 'FEMALE'), ('O', 'OTHERS')]
    gender = models.CharField(max_length=1, choices=genders)

