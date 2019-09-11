from services import *
from django.urls import reverse
from django.views.generic import DetailView, RedirectView, UpdateView
from django.contrib import messages
from django.utils.translation import ugettext_lazy as _
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render

def main_page(request):
    get_count_parties = get_count_reliant_parties()
    # Need to define HTML
    return render(request,'books.html', get_count_parties)