from django.urls import include, path
from django.views.generic.base import TemplateView
from . import views

urlpatterns = [
	path('', views.index, name='home'),
	path('product/', views.product, name='product'),
	path('product/<int:id>', views.productpage),
	path('contact/', views.contact, name='contact'),


	path('robots.txt', TemplateView.as_view(template_name="robots.txt", content_type="text/plain"))
	]
