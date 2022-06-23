from django import forms
from app.models import contact,schedule,apt,mail

class contactform(forms.ModelForm):
    name=forms.CharField(max_length=100)
    phone=forms.CharField(max_length=15)
    email=forms.CharField(max_length=80)
    subject=forms.CharField(max_length=250)
    message=forms.CharField(max_length=1000)
    class Meta:
        model=contact
        fields='__all__'
        
class scheduleform(forms.ModelForm):
    name=forms.CharField(max_length=100)
    phone=forms.CharField(max_length=15)
    time=forms.CharField(max_length=80)
    date=forms.CharField(max_length=250)
    pic=forms.ImageField()
    message=forms.CharField(max_length=1000)
    class Meta:
        model=schedule
        fields='__all__'
        
class aptform(forms.ModelForm):
    name=forms.CharField(max_length=100)
    phone=forms.CharField(max_length=15)
    email=forms.CharField(max_length=80)
    date=forms.CharField(max_length=250)
    time=forms.CharField(max_length=80)
    subject=forms.CharField(max_length=250)
    message=forms.CharField(max_length=1000)
    class Meta:
        model=apt
        fields='__all__'
        
class mailform(forms.ModelForm):
    email=forms.CharField(max_length=80)
    class Meta:
        model=mail
        fields='__all__'