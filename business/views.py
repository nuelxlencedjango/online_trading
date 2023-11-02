from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .models import * 
from account.models import *
from business.models import *
from django.contrib import messages
from django.utils import timezone
import random
import datetime
import time







def home(request): 

    return render(request,'others/index.html')




@login_required()
def tradingPlatform(request):
    trader = TradersDetails.objects.get(user = request.user)
   
    context ={"trader":trader}
    return render(request,'others/platform.html', context)





    
@login_required(login_url='/account/trader_login')
def user_transaction(request):
    try:
        trader = TradersDetails.objects.get(user=request.user)
        print('this is trader with username:',trader)

        if not trader:
            messages.warning(request, 'Trader profile not found. Please create a trader profile.')
            return redirect('account:register')

        balance = float(trader.current_balance)
        print("bal:", balance)

        if balance <= 0:
            messages.warning(request, 'Sorry, you need to add funds to your wallet')
            return redirect('traders:add_fund')


        # Simulate a trade every minute for 24 hours
        start_time = datetime.datetime.now()
        end_time = start_time + datetime.timedelta(hours=24)
        current_time = start_time

        while current_time <= end_time:
            
            # Simulate profit or loss
            profit_loss = float(round(random.uniform(-15, 20), 2))
            balance += profit_loss
            
            tradername =trader.user.first_name

            sno = tradername[:4] + str(uuid4())[:8]
            

            # Create a transaction record
            transaction = Biz.objects.create(trader=request.user, profit_loss=profit_loss,
                           date_of_transaction=timezone.now(),current_balance=balance,
                           referenceNo=sno)
            transaction.save()

            # Update the trader's balance
            trader.current_balance = balance
            trader.save()

            # Sleep for 1 minute
            current_time += datetime.timedelta(minutes=1)
            messages.warning(request, 'Please wait for 60 seconds.Your transactionis being progated!')
            time.sleep(30)
        
            return redirect('account:dash')

        messages.warning(request, 'Time has elapsed.')
        return redirect('account:dash')
    
    except TradersDetails.DoesNotExist:
        messages.warning(request, 'Trader profile not found. Please create a trader profile.')
        return redirect('account:register')





@login_required()
def bizTrading(request):
   
   
    context ={}
    return render(request,'others/platform.html', context)










