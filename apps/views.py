from django.views.generic import ListView, DetailView, TemplateView, CreateView, UpdateView
from django.shortcuts import render
from apps.models import Announcement, Category


class ProductLIstView(ListView):
    queryset = Announcement.objects.all()
    template_name = 'apps/main-page.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.filter(parent__isnull=True)
        context['vip_products'] = Announcement.objects.filter(product_type='vip').order_by('-created_at')[:8]
        context['regular_products'] = Announcement.objects.filter(product_type='simple').order_by('-created_at')[:16]
        return context


class CategoryLIstView(ListView):
    queryset = Category.objects.all()

