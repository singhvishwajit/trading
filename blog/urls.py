from django.urls import path, include
from .views import InvestingListView, InvestingDetailView, ContactCreateView, ResearchListView, ResearchDetailView, ProtocolListView, ProtocolDetailView
from . import views


urlpatterns = [
	path('', views.markets, name='blog-markets'),
	# path('about/', views.about, name='blog-about'),
	path('investing/', InvestingListView.as_view(), name="blog-investing"),
	path('research/', ResearchListView.as_view(), name="blog-researches"),
	path('protocols/', ProtocolListView.as_view(), name="blog-protocols"),
	path('resources/', views.resources, name='blog-resources'),
	path('news/', views.news, name='blog-news'),
	path('investing/<slug:slug>/', InvestingDetailView.as_view(), name='investing-detail'),
	path('research/<slug:slug>/', ResearchDetailView.as_view(), name='research-detail'),
	path('protocols/<slug:slug>/', ProtocolDetailView.as_view(), name='protocol-detail'),
	path('contact/', ContactCreateView.as_view(), name='blog-contact'),
	path('privacy/', views.privacy, name='blog-privacy'),
	path('terms/', views.terms, name='blog-terms'),
	path('contact/success', views.ContactSuccess, name='blog-contact-success'),
	path('tinymce/', include('tinymce.urls')),
]