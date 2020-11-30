from django import forms
# Create your models here.
class loginInfo(forms.Form):
    username= forms.CharField(label='username' ,max_length=25)
    password=forms.CharField(label='password' ,max_length=30)