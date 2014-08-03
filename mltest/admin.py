from django.contrib import admin
from mltest.models import Input

class InputAdmin(admin.ModelAdmin):
	list_display = ('id','raw_x', 'raw_y', 'raw_file')

admin.site.register(Input, InputAdmin)
