from .models import student
from django import forms

class studentform(forms.ModelForm):
    class Meta:
        model=student
        fields=['name','roll','email','password']
        widgets={
            'name':forms.TextInput(attrs={'class':'form-control','id':'nameid'}),
            'roll':forms.TextInput(attrs={'class':'form-control','id':'rollid'}),
            'email':forms.EmailInput(attrs={'class':'form-control','id':'emailid'}),
            'password':forms.PasswordInput(attrs={'class':'form-control','id':'passwordid'})
            
            }