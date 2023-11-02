
from django.db import models
from uuid import uuid4
from django.utils import timezone

from django.contrib.auth.models import User






class TradersDetails(models.Model):
    user = models.OneToOneField(User,null=True,blank=True, on_delete=models.CASCADE,related_name='trader')
    phone = models.CharField(max_length=200, null=True,blank=True)
    trader_id = models.CharField(max_length=50, null=True,blank=True)
    date_registered =models.DateField(default=timezone.now, null=True,blank=True)
    initial_balance = models.DecimalField(max_digits=50, decimal_places=2, default=100.00)
    current_balance = models.DecimalField(max_digits=50, decimal_places=2, default=100.00)
    


    def save(self, *args, **kwargs):
        if not self.trader_id:
            self.trader_id = self.user.username[:4] + str(uuid4())[:8]
            
        super(TradersDetails, self).save(*args, **kwargs)
   
  
    def __str__(self):

        return f"{self.user.username} - {self.user.first_name} - {self.user.last_name} - {self.current_balance}"
    

    class Meta:
        verbose_name_plural='Traders Detail'


        
    
        






 




