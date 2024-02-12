from django.urls import path

from plants import views

urlpatterns = (([
    path("beds/", views.BedListView.as_view(), name="bed_list"),
    path("beds/<int:pk>/", views.BedDetailView.as_view(), name="bed_detail"),
    path("plants/", views.PlantListView.as_view(), name="plant_list"),
    path("plants/<int:pk>/", views.PlantDetailView.as_view(), name="plant_detail"),
]))
