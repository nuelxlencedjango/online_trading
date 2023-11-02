
# traders/models.py
from django.db import models
from django.contrib.auth.models import User
from uuid import uuid4
from django.utils import timezone

from account.models import *




class Biz(models.Model):

    trader = models.ForeignKey(User, on_delete= models.CASCADE,related_name='bizman')
    profit_loss = models.DecimalField(max_digits=10, decimal_places=2, default=100.00)
    referenceNo = models.CharField(max_length=200, null=True,blank=True)
    date_of_transaction = models.DateTimeField(auto_now_add=True)
    current_balance = models.DecimalField(max_digits=50, decimal_places=2, default=100.00)
    

    def __str__(self):
        return str(self.trader)
    
    class Meta:  
        ordering = ['date_of_transaction']
    

