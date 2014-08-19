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

class PredictForm(forms.Form):

	yField = forms.CharField(
				label='Y',
				widget=forms.Textarea(attrs={					
					'class': 'form-control',
					'id': 'Y',
					'cols': 10,
					'rows': 1,
					'readonly': 'True'}),
				max_length=50,
				required=True)		

	def __init__(self, *args, **kwargs):
		self.n = kwargs.pop('n')
		super(PredictForm, self).__init__(*args, **kwargs)

		for i in xrange(1, self.n):
			self.fields[i] = forms.CharField(
				label='X' + str(i),
				widget=forms.Textarea(attrs={					
					'class': 'form-control',
					'id': 'X' + str(i),
					'cols': 10,
					'rows': 1}),
				max_length=50,
				required=True)			