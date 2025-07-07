from django.urls import path
from . import views

urlpatterns = [
    path('chart_view/', views.chart_view, name='charts'),
]