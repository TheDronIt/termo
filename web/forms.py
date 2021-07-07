from .models import Order, Message
from django.forms import ModelForm, TextInput, EmailInput, Textarea, CheckboxInput, RadioSelect, CheckboxSelectMultiple

class OrderForm(ModelForm):
	class Meta:
		model = Order
		fields = ['FIO', 'phone', 'email', 'client', 'tara', 'value', 'comment']

		widgets = {
			"FIO": TextInput(attrs={
					'class': 'form-text',
					'placeholder': 'Контактное лицо'
				}),
			"phone": TextInput(attrs={
					'class': 'form-text',
					'placeholder': 'Номер телефона'
				}),
			"email": EmailInput(attrs={
					'class': 'form-text',
					'placeholder': 'Почта'
				}),
			"client": EmailInput(attrs={
					'class': 'form-text',
					'placeholder': 'Реквизиты заказчика'
				}),
			"value": EmailInput(attrs={
					'class': 'form-text',
					'placeholder': 'Количество'
				}),
			"comment": Textarea(attrs={
					'class': 'form-text-big',
					'placeholder': 'Комментарий'
				}),
		}

class MessageForm(ModelForm):
	class Meta:
		model = Message
		fields = ['FIO', 'phone', 'email', 'comment']

		widgets = {
			"FIO": TextInput(attrs={
					'class': 'form-text',
					'placeholder': 'ФИО'
				}),
			"phone": TextInput(attrs={
					'class': 'form-text',
					'placeholder': 'Номер телефона'
				}),
			"email": EmailInput(attrs={
					'class': 'form-text',
					'placeholder': 'Почта'
				}),
			"comment": Textarea(attrs={
					'class': 'form-text-big',
					'placeholder': 'Комментарий'
				})
		}