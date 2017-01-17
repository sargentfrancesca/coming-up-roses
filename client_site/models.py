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
	treatment_descripton = models.TextField(null=True)
	category = models.ForeignKey(Category, on_delete=models.CASCADE)

	def __str__(self):
		return "%s: %s" % (self.treatment_name, self.treatment_price)

class MailingList(models.Model):
	user_name = models.CharField(max_length=100)
	user_email = models.EmailField(max_length=254)

	def __str__(self):
		return "%s: %s" % (self.user_name, self.user_email)

class Images(models.Model):
	image_filename = models.CharField(max_length=100)
	image_title = models.CharField(max_length=64)
	image_description = models.TextField(null=True)

	def __str__(self):
		return "%s: %s [%s]" % (self.image_filename, self.image_title, self.image_description)

	