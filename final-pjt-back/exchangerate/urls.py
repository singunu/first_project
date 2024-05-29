from django.urls import path
from . import views

urlpatterns = [
    path('exchange/', views.save_exchange_rate),
    path('get-exchange/', views.get_exchange_rate)
]