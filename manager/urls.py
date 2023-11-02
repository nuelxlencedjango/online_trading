
from django.urls import path
from . import views




app_name = 'manager'

urlpatterns =[
     path('admin_dashboard/',views.adminDashboard, name='admin_dashboard'),
      path('user_data/<int:pk>/',views.userTransactionDetails, name='user_data'),
       path('no_info/',views.user_not_found, name='no_info'),
]





