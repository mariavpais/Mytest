from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Dashboards(models.Model):
	title = models.CharField(max_length=100)
	content = models.TextField()
	image = models.ImageField()
	date_posted = models.DateTimeField(default=timezone.now)

	def __str__(self):
		return self.title