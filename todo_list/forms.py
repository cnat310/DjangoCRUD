from django import forms
from .models import List

class ListForm(forms.ModelForm):
	class Meta:
		model = List
		fields = ["priority", "system", "task", "procedure", "notes", "owner", "date", "status"]

class DateForm(forms.ModelForm):
	class Meta:
		model = List
		fields = ["date"]