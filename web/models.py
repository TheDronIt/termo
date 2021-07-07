from django.db import models
from django import forms

class Order(models.Model):

	TARA = [
		('Значение 1', 'Значение 1'),
		('Значение 2', 'Значение 2')
	]

	FIO = models.CharField(max_length = 120)
	phone = models.CharField(max_length = 60)
	email = models.EmailField()
	client = models.CharField(max_length = 60)
	tara = models.CharField(max_length=300, choices = TARA)
	value = models.CharField(max_length = 20)
	comment = models.TextField()

	def __str__(self):
		return str(self.id)+" | "+str(self.FIO)

class Message(models.Model):
	FIO = models.CharField(max_length = 120)
	phone = models.CharField(max_length = 60)
	email = models.EmailField()
	comment = models.TextField()
	
	def __str__(self):
		return str(self.id)+" | "+str(self.FIO)

class Product(models.Model):
	name = models.CharField(max_length = 120)
	img = models.ImageField(upload_to='product/', blank=True)
	sort = models.CharField(max_length = 120)
	gryz = models.CharField(max_length = 120)
	width = models.CharField(max_length = 120)
	length = models.CharField(max_length = 120)
	height = models.CharField(max_length = 120)
	material = models.CharField(max_length = 120)
	thickness = models.CharField(max_length = 120)
	stamp = models.CharField(max_length = 120)
	doc = models.CharField(max_length = 120)
	price = models.CharField(max_length = 120)
	
	def __str__(self):
		return str(self.id)+" | "+str(self.name)