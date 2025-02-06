# yourapp/forms.py
from django import forms
from .models import Workwithus

class Workwithus(forms.ModelForm):
    class Meta:
        model = Workwithus
        fields = ['name','mobile','email','company','field_of_work','desc','webap','app']
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['webap'].widget = forms.CheckboxInput(attrs={'class': 'checkbox'})
        self.fields['app'].widget = forms.CheckboxInput(attrs={'class': 'checkbox'})