from django.views.generic import DetailView, ListView
from .models import Bed, JournalEntry, Plant, Planting


class BedListView(ListView):
    model = Bed
    template_name = "plants/bed_list.html"

    def get_queryset(self):
        return Bed.objects.all()


class BedDetailView(DetailView):
    model = Bed
    template_name = "plants/bed_detail.html"


class PlantListView(ListView):
    model = Plant
    template_name = "plants/plant_list.html"

    def get_queryset(self):
        return Plant.objects.all()


class PlantDetailView(DetailView):
    model = Plant
    template_name = "plants/plant_detail.html"
