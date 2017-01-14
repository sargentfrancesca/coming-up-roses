from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Category(models.Model):
	category_name = models.CharField(max_length=100)
	category_description = models.TextField()

	def __str__(self):
		return "%s (%s)" % (self.category_name, self.category_description)

class Treatment(models.Model):
	treatment_name = models.CharField(max_length=100)
	treatment_price = models.DecimalField(max_digits=5, decimal_places=2)
	category = models.ForeignKey(Category, on_delete=models.CASCADE)

	def __str__(self):
		return "%s: %s" % (self.treatment_name, self.treatment_price)