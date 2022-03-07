from django.shortcuts import render
import requests
import pandas as pd
import math
from django.core.paginator import Paginator
from .models import Investing, Research, Protocol, Contact, Category
from django.views.generic import ListView, DetailView, CreateView

def home(request):
	# context = {
	# 	'tradings': Trading.objects.all() [:4]
	# }
	return render(request, 'blog/home.html')

def resources(request):
	return render(request, 'blog/resources.html', {'title': 'Resources'})

def algorithms(request):
	api_url = 'https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&order=market_cap_desc&per_page=100&page=125&sparkline=false'
	data = requests.get(api_url).json()
	context = {
	'data': data,
	}
	return render(request, 'blog/algorithms.html', context)

def privacy(request):
	return render(request, 'blog/privacy.html', {'title': 'Privacy'})

def terms(request):
	return render(request, 'blog/terms.html', {'title': 'Terms of Use'})

def markets(request):
	api_defi_url = 'https://api.coingecko.com/api/v3/global/decentralized_finance_defi'
	defi = requests.get(api_defi_url).json()
	api_url = 'https://api.coingecko.com/api/v3/coins/markets?vs_currency=USD&order=market_cap_desc&per_page=100&page=1&sparkline=false'
	data = requests.get(api_url).json()
	api_overall_url = 'https://api.coingecko.com/api/v3/global'
	overall = requests.get(api_overall_url).json()
	context = {
		'data': data,
		'defi': defi,
		'overall': overall,
	}

	return render(request, 'blog/markets.html', context)

def news(request):
	api_news = 'https://data.messari.io/api/v1/news'
	news = requests.get(api_news).json()
	return render(request, 'blog/news.html', {'news': news})

class InvestingDetailView(DetailView):
	model = Investing

class ResearchDetailView(DetailView):
	model = Research

class ProtocolDetailView(DetailView):
	model = Protocol

class ContactCreateView(CreateView):
    model = Contact
    fields = ['name', 'email', 'subject', 'message']
    success_url = 'success'

def ContactSuccess(request):
	return render(request, 'blog/contact_success.html', {'title': 'Contact'})

# def articles(request):
# 	context = {
# 		'posts': Post.objects.all(),
# 		'title': 'Notes'
# 	}
# 	return render(request, 'blog/articles.html', context)

class InvestingListView(ListView):
	model = Investing
	template_name = 'blog/investing.html' # <app>/<model>_<viewtype>.html
	context_object_name = 'investings'
	ordering = ['-date_posted']
	paginate_by = 6
	def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        	context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        	
        	context['title'] = 'Investing'
        	return context


class ResearchListView(ListView):
	model = Research
	template_name = 'blog/research.html' # <app>/<model>_<viewtype>.html
	context_object_name = 'researches'
	ordering = ['-date_posted']
	paginate_by = 6
	def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        	context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        	
        	context['title'] = 'Research'
        	return context

class ProtocolListView(ListView):
	model = Protocol
	template_name = 'blog/protocol.html' # <app>/<model>_<viewtype>.html
	context_object_name = 'protocols'
	ordering = ['-date_posted']
	paginate_by = 6
	def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        	context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        	
        	context['title'] = 'Protocols'
        	return context
