from django.urls import path
from . import views

from management_ui.users.views import (
    user_redirect_view,
    user_update_view,
    user_detail_view,
)

app_name = "apiviews"
urlpatterns = [
    path("", views.main_page, name="main"),
]
