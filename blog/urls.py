from django.urls import path, include
from .views import TradingListView, TradingDetailView, ContactCreateView, DeFiListView, DeFiDetailView, ProjectListView, ProjectDetailView, BlockchainListView, BlockchainDetailView
from . import views


urlpatterns = [
	path('', views.home, name='blog-home'),
	# path('about/', views.about, name='blog-about'),
	path('trading/', TradingListView.as_view(), name="blog-trading"),
	path('defi/', DeFiListView.as_view(), name="blog-defi"),
	path('blockchain/', BlockchainListView.as_view(), name="blog-blockchain"),
	path('projects/', ProjectListView.as_view(), name="blog-projects"),
	path('resources/', views.resources, name='blog-resources'),
	path('trading/<slug:slug>/', TradingDetailView.as_view(), name='trading-detail'),
	path('defi/<slug:slug>/', DeFiDetailView.as_view(), name='defi-detail'),
	path('blockchain/<slug:slug>/', BlockchainDetailView.as_view(), name='blockchain-detail'),
	path('project/<slug:slug>/', ProjectDetailView.as_view(), name='project-detail'),
	path('contact/', ContactCreateView.as_view(), name='blog-contact'),
	path('privacy/', views.privacy, name='blog-privacy'),
	path('terms/', views.terms, name='blog-terms'),
	path('contact/success', views.ContactSuccess, name='blog-contact-success'),
	path('tinymce/', include('tinymce.urls')),
]