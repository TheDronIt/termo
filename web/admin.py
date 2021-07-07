from django.contrib import admin
from .models import Order, Message, Product
from django import forms

admin.site.register(Order)
admin.site.register(Message)
admin.site.register(Product)

