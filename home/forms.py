# forms.py
from django import forms
from .models import YourModel,newform

class YourModelForm(forms.ModelForm):
    class Meta:
        model = YourModel
        fields = ['title', 'price', 'image']


class CartItemForm(forms.Form):
    quantity = forms.IntegerField(
        label='Quantity',
        min_value=1,
        required=True,
        widget=forms.NumberInput(attrs={'class': 'form-control'})
    )

class PriceFilterForm(forms.Form):
    min_price = forms.DecimalField(min_value=0, required=False, label='Min Price')
    max_price = forms.DecimalField(min_value=0, required=False, label='Max Price')


class registerform(forms.ModelForm):
    class Meta:
        model=newform
        fields="__all__"

class simpleform(forms.Form):
    fname=forms.CharField(max_length=50,required=True,label="First name")
    lname=forms.CharField(max_length=50,required=True,label="Last name")
    passw= forms.CharField(max_length=50, required=True,label="Password")
    age1=forms.IntegerField(required=True,label="Age")
    email1=forms.EmailField(required=True,label="Email")
    address1=forms.CharField(required=True,label="Address",widget=forms.Textarea(attrs={'rows': 10}))
    phno=forms.IntegerField(required=True,label="Phone-Number")
    genders = [('M', 'MALE'), ('F', 'FEMALE'), ('O', 'OTHERS')]
    gen=forms.ChoiceField(choices=genders,label="Gender")
    # prescriptions=forms.FileField()

class newlog(forms.Form):
    email1=forms.EmailField(required=True,label="Email")
    passw= forms.CharField(required=True,label="Password")
    
class otpverif(forms.Form):
    # email1=forms.EmailField(required=True,label="Email")
    otp= forms.IntegerField(required=True,label="OTP")
