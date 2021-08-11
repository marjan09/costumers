from django import forms
from .models import InsertToDb

class PersonData(forms.ModelForm):
	class Meta:
		model = InsertToDb
		fields = '__all__'
  
  