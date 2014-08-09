import os.path
from django.db import models
from django.dispatch import receiver

class Input(models.Model):
	raw_x = models.CharField(max_length=1000)
	raw_y = models.CharField(max_length=1000)
	raw_file = models.FileField(upload_to='raw_files')

	def filename(self):
		return os.path.basename(self.raw_file.name) 

# Remove local file if it's deleted from db
@receiver(models.signals.post_delete, sender=Input)
def delete_handler(sender, instance, **kwargs):
	if instance.raw_file and os.path.isfile(instance.raw_file.path):
		os.remove(instance.raw_file.path)
		
	
