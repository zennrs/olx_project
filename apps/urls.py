from django.urls import path
from apps.views import ProductLIstView


urlpatterns = [
    path('', ProductLIstView.as_view(), name='olx.uz'),
]
