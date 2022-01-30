from django.shortcuts import render
from django.core.paginator import Paginator
from .models import Trading, DeFi, Investment, Contact, Blockchain
from django.views.generic import ListView, DetailView, CreateView

def home(request):
	context = {
		'tradings': Trading.objects.all() [:4]
	}
	return render(request, 'blog/home.html', context)

# def about(request):
# 	return render(request, 'blog/about.html', {'title': 'About'})

# def projects(request):
# 	return render(request, 'blog/projects.html', {'title': 'Projects'})

def resources(request):
	return render(request, 'blog/resources.html', {'title': 'Resources'})

def privacy(request):
	return render(request, 'blog/privacy.html', {'title': 'Privacy'})

def terms(request):
	return render(request, 'blog/terms.html', {'title': 'Terms of Use'})


class TradingDetailView(DetailView):
	model = Trading

class DeFiDetailView(DetailView):
	model = DeFi

class InvestmentDetailView(DetailView):
	model = Investment

class BlockchainDetailView(DetailView):
	model = Blockchain

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

class TradingListView(ListView):
	model = Trading
	template_name = 'blog/trading.html' # <app>/<model>_<viewtype>.html
	context_object_name = 'tradings'
	ordering = ['-date_posted']
	# paginate_by = 6
	def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        	context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        	
        	context['title'] = 'Trading Notes'
        	return context


class DeFiListView(ListView):
	model = DeFi
	template_name = 'blog/defi.html' # <app>/<model>_<viewtype>.html
	context_object_name = 'defis'
	ordering = ['-date_posted']
	# paginate_by = 6
	def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        	context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        	
        	context['title'] = 'DeFi Notes'
        	return context

class InvestmentListView(ListView):
	model = Investment
	template_name = 'blog/investment.html' # <app>/<model>_<viewtype>.html
	context_object_name = 'investments'
	ordering = ['-date_posted']
	# paginate_by = 6
	def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        	context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        	
        	context['title'] = 'Investment Notes'
        	return context

class BlockchainListView(ListView):
	model = Blockchain
	template_name = 'blog/blockchain.html' # <app>/<model>_<viewtype>.html
	context_object_name = 'blockchains'
	ordering = ['-date_posted']
	# paginate_by = 6
	def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        	context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        	
        	context['title'] = 'Blockchain Notes'
        	return context