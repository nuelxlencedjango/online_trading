
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

from .forms import *
from .models import * 
from business.models import Biz

import plotly.express as px
import pandas as pd

from django.shortcuts import render, redirect

from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required




#registration
def registerPage(request):
    cnt = TradersDetails.objects.all().count()
    if cnt <= 9:
        if request.method == 'POST':
       
            form1 = SignUpForm(request.POST)
            form2 = TradersDetailsForm(request.POST)
         
            #check data given validity
            if form1.is_valid() and form2.is_valid():
                user = form1.save()

                #associate detail information to the user before saving
                profile = form2.save(commit=False)
                profile.user =user
                profile.save()

                name = form1.cleaned_data.get('username')
                messages.success(request, 'Account successfully created ' , name)

                return redirect('account:trader_login')
        
            else:
                form1 = SignUpForm(request.POST)
                form2 = TradersDetailsForm(request.POST)

                messages.warning(request, 'There was a problem in the form') 
                context = {'form1':form1, 'form2': form2} 
                return render(request, 'acct/signup.html', context)
            

        form1 = SignUpForm()
        form2 = TradersDetailsForm()           
        context = {'form1':form1, 'form2': form2,"cnt":cnt}   
        return render(request, 'acct/signup.html', context)
    
    ex ="excess"
    context={"cnt":cnt, "ex":ex}
    return render(request, 'acct/signup.html', context)





# login
def login_view(request):
    form = TradersLoginForm()
    error = "" 
    
    if request.method == 'POST':
        form = TradersLoginForm(data=request.POST)
       
        # Check input validity
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            
            # Authenticate username and password
            user = authenticate(request, username=username, password=password)
 
            if user is not None:
                if user.is_superuser:
                    login(request, user)
                    return redirect('manager:admin_dashboard')
                 
                
                login(request, user)

                return HttpResponseRedirect(reverse('account:dash'))
            else:
                return render(request, 'acct/signin.html', context={'form': form, 'user': "Customer Login", 'error': 'Invalid username or password'})
        else:
            error = 'Invalid username or password' 

    context = {'form': form, 'error': error}
    return render(request, 'acct/signin.html', context)



#log out
@login_required()
def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('business:home'))







@login_required()
def dashboard(request):
    
    traderData = TradersDetails.objects.filter(user=request.user)
    if Biz.objects.filter(trader=request.user).exists():
        data = Biz.objects.filter(trader=request.user)

        df = pd.DataFrame(list(data.values()))

        fig = px.line(df, x="date_of_transaction", y="current_balance", title="Transaction Data", hover_data=["profit_loss"])
        fig2 = px.bar(df, x="date_of_transaction", y="current_balance", title="Transaction Data", hover_data=["profit_loss"])

        # Convert the figure to HTML
        graph_html = fig.to_html()
        graph_html2 = fig2.to_html()
   
        context={'traderData':traderData,"graph_html": graph_html,'data':data, "graph_html2":graph_html2}
        return render(request, "acct/dashboard.html", context)
    
    context={'traderData':traderData}
    return render(request, "acct/dashboard.html", context)



#log out
@login_required()
def funding(request):
    
    return render(request, 'acct/funds.html.html')



@login_required()
def deleteUser(request, pk):
    trader = TradersDetails.objects.get(pk=pk)
    user = trader.user  
    user.delete()
    
    return redirect('manager:admin_dashboard')



