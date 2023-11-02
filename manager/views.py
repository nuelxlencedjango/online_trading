
from django.shortcuts import render,redirect

from django.contrib import messages

from .forms import *
from  account.models import * 
from business.models import Biz


import plotly.express as px
import pandas as pd
from django.shortcuts import get_object_or_404

from django.contrib.auth.decorators import login_required





  









@login_required()
def userTransactionDetails(request, pk):
    try:
        trader = get_object_or_404(TradersDetails, pk=pk)
        if Biz.objects.filter(trader=trader.user).exists():
            businessInfo = Biz.objects.filter(trader=trader.user)

            df = pd.DataFrame(list(businessInfo.values()))
            fig = px.line(df, x="profit_loss", y="current_balance", title="Traders Transaction Information", hover_data=["date_of_transaction"])
            fig2 = px.bar(df, x="profit_loss", y="current_balance", title="Traders Transaction Information", hover_data=["date_of_transaction"])

            # Convert the figure to HTML
            graph_html = fig.to_html()
            graph_html2 = fig2.to_html()
        else:
            messages.warning(request, "User has no transaction details yet.")
            return redirect('manager:no_info')
        

    except TradersDetails.DoesNotExist:
        trader = None
        businessInfo = None
        graph_html = graph_html2 = None

    context = {"businessInfo": businessInfo, 'trader': trader, 'graph_html': graph_html, 'graph_html2': graph_html2}
    return render(request, "acct/userTransaction.html", context)




def user_not_found(request):
    return render(request, "acct/userTransaction.html")






@login_required()
def adminDashboard(request):

    tradersData = TradersDetails.objects.all()
    tradeCount = tradersData.count()

    data = Biz.objects.all()
    dataCount = data.count()

    if tradeCount > 0:
        df = pd.DataFrame(list(tradersData.values()))
        fig = px.line(df, x="trader_id", y="current_balance", title="Traders Transaction Information", hover_data=["initial_balance"])
        fig2 = px.bar(df, x="trader_id", y="current_balance", title="Traders Transaction Information", hover_data=["initial_balance"])

        # Convert the figure to HTML
        graph_html = fig.to_html()
        graph_html2 = fig2.to_html()

        context = {
            'tradersData': tradersData,
            "graph_html": graph_html,
            'data': data,
            "graph_html2": graph_html2,
            'tradeCount': tradeCount,
            'dataCount': dataCount
        }
    else:
        context = {
            'tradersData': tradersData,
            'tradeCount': tradeCount,
            'dataCount': dataCount
        }

    return render(request, "acct/admin.html", context)

