import os.path
from django.db import models

class Input(models.Model):
	raw_x = models.CharField(max_length=1000)
	raw_y = models.CharField(max_length=1000)
	raw_file = models.FileField(upload_to='raw_files')

	def filename(self):
		return os.path.basename(self.raw_file.name) 