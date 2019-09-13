from django.urls import path
from . import views

app_name = "apiviews"
urlpatterns = [
    path("", views.main_page, name="main"),
    path("parties/<status>", views.list_parties, name="parties"),
    path("party/<id>", views.detail_party, name="partydetail"),
    path("party/", views.update_create_party, name="partycreateupdate"),
]
