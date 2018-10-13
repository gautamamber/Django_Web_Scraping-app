from django.shortcuts import render
# converted into json
import json
# request the api
import  requests
# Create your views here.

def home(request):
	# crypto price data
	price_request = requests.get("https://min-api.cryptocompare.com/data/pricemultifull?fsyms=BTC,XRP&tsyms=USD,EUR")
	price = json.loads(price_request.content.decode('utf-8'))
	# cryptocompare news api
	api_request = requests.get("https://min-api.cryptocompare.com/data/v2/news/?lang=EN")
	api = json.loads(api_request.content.decode('utf-8'))
	return render(request, "webapp/home.html" , {'api' : api, 'price' : price}) 
