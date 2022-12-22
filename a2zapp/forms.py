from a2zapp.models import empmodel, news, calender
from django import forms
class empform(forms.ModelForm):
    class Meta:
        model = empmodel
        fields = '__all__'
class newsform(forms.ModelForm):
    class Meta:
        model = news
        fields = '__all__'
class calenderform(forms.ModelForm):
    class Meta:
        model = calender
        fields='__all__'

