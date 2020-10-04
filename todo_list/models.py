from django.db import models
from datetime import datetime, date

class List(models.Model):
	priority = models.CharField(max_length=50)
	system = models.CharField(max_length=50)
	task = models.CharField(max_length=50)
	procedure = models.CharField(max_length=50)
	notes = models.CharField(max_length=500)
	owner = models.CharField(max_length=50)
	date = models.DateField(blank=True, null=True)
	status = models.CharField(max_length=50, blank=True, null=True)

	def __str__(self):
		return self.procedure