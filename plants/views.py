from django.shortcuts import render
from django.views.generic import DetailView, ListView
from .models import Bed, JournalEntry, Plant, Planting


def home(request):
    beds = Bed.objects.all()
    return render(request, "plants/home.html", context={"beds": beds})


class BedListView(ListView):
    model = Bed
    template_name = "plants/bed_list.html"


class BedDetailView(DetailView):
    model = Bed
    template_name = "plants/bed_detail.html"


class PlantListView(ListView):
    model = Plant
    template_name = "plants/plant_list.html"


class PlantDetailView(DetailView):
    model = Plant
    template_name = "plants/plant_detail.html"
