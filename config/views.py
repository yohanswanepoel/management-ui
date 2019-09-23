from django.urls import reverse
from django.views.generic import DetailView, RedirectView, UpdateView
from django.contrib import messages
from django.utils.translation import ugettext_lazy as _
from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404, render, redirect
import json

def main_page(request):
    # Need to define HTML
    if request.user is not None and request.user.is_active:
        print(reverse("management:main"))
        return redirect(reverse("management:main"))
    else:
        return render(request,'pages/home.html')

def health(request):
    data = {
        'status': 'healthy'
    }
    return JsonResponse(data)