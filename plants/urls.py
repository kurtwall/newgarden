from django.urls import path

from plants import views

urlpatterns = (([
    path("", views.index, name="index"),
    path("beds/", views.BedListView.as_view(), name="bed_list"),
    path("beds/<bed>/", views.bed_detail_view, name="bed_detail"),
    path("journal/", views.JournalEntryListView.as_view(), name="journalentry_list"),
    path("journal/<int:pk>/", views.JournalEntryDetailView.as_view(), name="journalentry_detail"),
    path("plants/", views.PlantListView.as_view(), name="plant_list"),
    path("plants/<int:pk>/", views.PlantDetailView.as_view(), name="plant_detail"),
]))
