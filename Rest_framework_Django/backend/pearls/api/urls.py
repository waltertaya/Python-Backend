from django.urls import path
from . import views


urlpatterns = [
    path('', views.product),
    path('all/', views.all_products)
]
