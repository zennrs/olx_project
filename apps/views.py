from django.views.generic import ListView, DetailView, TemplateView, CreateView, UpdateView
from django.shortcuts import render
from apps.models import Product

class ProductLIstView(ListView):
    queryset = Product.objects.all()
    template_name = 'apps/main-page.html'



