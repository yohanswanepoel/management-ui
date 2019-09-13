from . import services
from .forms import ProviderForm
from django.urls import reverse
from django.views.generic import DetailView, RedirectView, UpdateView
from django.contrib import messages
from django.utils.translation import ugettext_lazy as _
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
import json

def main_page(request):
    # New
    # Testing
    # Active
    # Down
    # Retired
    parties = {}
    parties['New'] = services.get_count_reliant_parties("New")
    parties['Alpha'] = services.get_count_reliant_parties("Alpha")
    parties['Beta'] = services.get_count_reliant_parties("Beta")
    parties['Active'] = services.get_count_reliant_parties("Active")
    parties['Down'] = services.get_count_reliant_parties("Down")
    parties['Retired'] = services.get_count_reliant_parties("Retired")
    # Need to define HTML
    context = {
        'parties_count' : parties
    }
    return render(request, 'base_logged_in.html', context)

def testing(request, task):
    result = 'None'
    if task == "clear_parties":
        result = services.delete_all_parties()
    elif task == "load_providers":
        result = services.load_providers()
    context = {
        'messages': [result]
    }
    return render(request, 'test/test_page.html', context)

def test_page(request):
    return render(request, 'test/test_page.html')

def list_parties(request, status):
    # New
    # Testing
    # Active
    # Down
    # Retired
    print(request)
    filter_field = status
    parties = services.get_parties(filter_field)
    # Need to define HTML
    context = {
        'filter' : filter_field,
        'parties' : parties
    }
    return render(request, 'reliantparties/list.html', context)

def detail_party(request, id):
    if request.method == 'POST':
        form = ProviderForm(request.POST)
        if form.is_valid():
            pass  # does nothing, just trigger the validation
    else:
        if id is None:
            form = ProviderForm()
        else:
            party = services.get_party(id)
            form = ProviderForm(initial=party)

    # Need to define HTML
    context = {
        'form' : form
    }
    return render(request, 'reliantparties/detail.html', context)

def update_create_party(request):
    if request.method == 'POST':
        form = ProviderForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            print(data)
            resp_dat = services.update_create_party(data)
            form = ProviderForm(initial=resp_dat)
    else:
        form = ProviderForm()

    # Need to define HTML
    context = {
        'form' : form
    }
    return render(request, 'reliantparties/detail.html', context)