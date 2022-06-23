from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.

class homeview(TemplateView):
    template_name="home.html"
class aboutview(TemplateView):
	template_name="about.html"
