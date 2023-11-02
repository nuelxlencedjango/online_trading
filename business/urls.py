

from django.urls import path
#from .views import *
from . import views




app_name = 'business'

urlpatterns =[
    path('',views.home, name='home'),
     path('businessTrading/',views.tradingPlatform, name='businessTrading'),
     path('platform/',views.user_transaction, name='platform'),
   
    
]
   




