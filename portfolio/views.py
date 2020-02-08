from django.shortcuts import render
from django.views import generic
from .models import Portfolio


def index(request):
    posts = Portfolio.objects.all()
    context = {'posts': posts}
    return render(request, 'portfolio/index.html', context)


class PortfolioDetail(generic.DetailView):
    model = Portfolio
    template_name = 'portfolio/portfolio_detail.html'
