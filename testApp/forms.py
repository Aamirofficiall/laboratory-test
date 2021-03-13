from django import forms  
from .models import *


class DateInput(forms.DateInput):
    input_type = 'date'

class TestReportForm(forms.ModelForm):  
    class Meta:  
        model = TestReport  
        exclude = ('user','id')
        widgets = {
            'date_created': DateInput() 
        }        
