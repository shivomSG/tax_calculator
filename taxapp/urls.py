from django.urls import path
from .views import tax_view

urlpatterns = [
    path('', tax_view, name='tax_view'),
]
