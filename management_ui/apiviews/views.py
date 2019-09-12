from . import services
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