from django.shortcuts import render, redirect
from .models import Order, Message, Product
from .forms import OrderForm, MessageForm

def index(request):
	return render(request, 'index.html') 

def product(request):
	error = ''
	if request.method == 'POST':
		form = OrderForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('home')
		else:
			error = 'Ошибка заполнения формы'

	form = OrderForm()
	product = Product.objects.all()
	data = {
		'form': form,
		'error': error,
		'product': product
	}
	return render(request, 'product.html', data) 

def contact(request):
	error = ''
	if request.method == 'POST':
		form = MessageForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('home')
		else:
			error = 'Ошибка заполнения формы'

	form = MessageForm()
	data = {
		'form': form,
		'error': error
	}
	return render(request, 'contact.html', data)

def productpage(request, id):
	productpage = Product.objects.get(id=id)
	
	return render(request, 'productpage.html', {'productpage':productpage})

