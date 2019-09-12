from django.urls import path
from . import views

app_name = "apiviews"
urlpatterns = [
    path("", views.main_page, name="main"),
    path("parties/<status>", views.list_parties, name="parties"),
    path("party/<pk>", views.detail_party, name="partydetail"),
]
