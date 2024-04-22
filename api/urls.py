from django.urls import path
from .views import PartyView,PartyUpdateView,EntryView

urlpatterns = [
    path("party",PartyView.as_view(),name="party"),
    path("party/<str:party_id>",PartyUpdateView.as_view(),name="party_delete"),
    path("entry",EntryView.as_view(),name="entry_details")
]
