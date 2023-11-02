
from django.urls import path
from . import views




app_name = 'account'

urlpatterns =[
     path('trader_login/', views.login_view, name='trader_login'),
    path('signup/', views.registerPage, name='signup'),
    path('trader_logout', views.logout_view, name='trader_logout'),
    path('dash/', views.dashboard, name='dash'),
    path('add_fund/',views.funding, name='add_fund'),
    path('delete_user/<int:pk>/',views.deleteUser, name='delete_user'),
]


