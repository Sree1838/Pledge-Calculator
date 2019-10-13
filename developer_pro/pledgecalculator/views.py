from django.shortcuts import render
from .models import Stock_details
import urllib.request
import re


# Create your views here.
def index(request):
    return render(request, 'index.html')

def listToString(s):
    str1 = " "
    return (str1.join(s))

def stockprice():
    stock = ans
    stock = str(stock)
    hdr = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3', 'Accept-Encoding': 'none',
        'Accept-Language': 'en-US,en;q=0.8', 'Connection': 'keep-alive'}
    url = urllib.request.Request(
        "https://www.nseindia.com/live_market/dynaContent/live_watch/get_quote/GetQuote.jsp?symbol=" + stock + "&illiquid=0&smeFlag=0&itpFlag=0",
        headers=hdr)
    nav = urllib.request.urlopen(url)
    data = nav.read()
    srch = '"lastPrice":"(.+?)"'
    com = re.compile(srch)
    global rslt
    rslt = re.findall(com, str(data))
    rslt = listToString(rslt)
   # if (rslt):
   #     print("last price : " + str(rslt))
    return ({'Result' : rslt})

def calc(request):
    if request.method == 'POST':
        print("POST")
        fname_r = request.POST.get('fname')
        lname_r = request.POST.get('lname')
        email_r = request.POST.get('email')
        sname_r = request.POST.get('sname')
        sprice_r = request.POST.get('sprice')
        nshares_r = int(request.POST.get('nshares'))
        print(type(sprice_r))
        sprice_r = float(sprice_r)
        share_value = sprice_r * nshares_r
        pledge_r = (sprice_r * nshares_r) * 0.5
        print(pledge_r)
        return render(request, 'output.html', {'Result': pledge_r, 'ShareValue': share_value})
    else:
        print("GET")
        global ans
        ans = request.GET['Stock Name']
        print(ans)
        stockprice()
        print(rslt)
        r = rslt.replace(',', '')
        return render(request, 'calc.html', {'answ': ans, 'result' : r})
def stocks(request):
    if request.method == 'POST':
        print("POST")
       # global stock_names
        stock_names = Stock_details.objects.all()
        print(stock_names)

        return render(request, 'stocks.html', {'stockNames': stock_names})
    else:
        print("GET")
        names = []
        stock_names = Stock_details.objects.all()
        print(stock_names)
        for name in stock_names:
            names.append(name)
        print(names)
        return render(request, 'stocks.html', {'stockNames': names})

