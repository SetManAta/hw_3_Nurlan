from django.shortcuts import render
from django.views import generic
from .models import Client,Credit,Account

class ListView(generic.ListView):
    model = Client
    template_name = 'index.html'
    context_object_name = 'client_list'


class ClientDetailView(generic.DetailView):
    model = Client
    template_name = 'detail.html'
    context_object_name = 'client'
