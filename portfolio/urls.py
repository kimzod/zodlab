from django.urls import path
from . import views

app_name = 'portfolio'
urlpatterns = [
    path('', views.index, name='index'),
    path('portfolio/<slug:slug>/', views.PortfolioDetail.as_view(), name='portfolio_detail'),
]