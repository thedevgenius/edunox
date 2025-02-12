from django.shortcuts import render
from django.views.generic import TemplateView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

# Create your views here.
class HomeView(TemplateView):
    template_name = 'core/index.html'

@method_decorator(login_required, name='dispatch')
class DashboardView(TemplateView):
    template_name = 'core/dashboard.html'