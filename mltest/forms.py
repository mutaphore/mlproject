from django import forms
from mltest.models import Input

class InputForm(forms.ModelForm):
	raw_x = forms.CharField(
		widget=forms.Textarea(attrs={
			'class': 'form-control', 
			'cols': 100, 
			'rows': 10}), 
		max_length=10000, 
		help_text="X",
		required=False)

	raw_y = forms.CharField(
		widget=forms.Textarea(attrs={
			'class': 'form-control',
			'cols': 100, 
			'rows': 10}), 
		max_length=10000, 
		help_text="Y",
		required=False)

	raw_file = forms.FileField(required=False)

	class Meta:
		model = Input
		fields = ('raw_x', 'raw_y', 'raw_file')