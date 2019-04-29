from django.urls import path
from .views import home

core_patterns = ([
    path('', home.as_view(), name='home'),  
], 'core')


