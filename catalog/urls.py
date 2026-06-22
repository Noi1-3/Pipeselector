from django.urls import path
from .views import home, calculator, pipe_list, valve_list, pipe_detail, valve_detail

urlpatterns = [
    path('', home, name='home'),
    path('calculator/', calculator, name='calculator'),
    path('pipes/', pipe_list, name='pipe_list'),
    path('valves/', valve_list, name='valve_list'),
    path('pipe/<int:id>/', pipe_detail, name='pipe_detail'),
    path('valve/<int:id>/', valve_detail, name='valve_detail'),
]