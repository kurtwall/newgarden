from django.shortcuts import render
from django.views.generic import DetailView, ListView
from .models import Bed, JournalEntry, Plant, Planting, Task


class BedListView(ListView):
    model = Bed
    template_name = "plants/bed_list.html"


def bed_detail_view(request, bed):
    bed_detail = Planting.objects.filter(bed_id=bed)
    is_raised = Bed.objects.get(bed=bed).is_raised
    context = {'bed': bed, 'is_raised': is_raised, 'bed_detail': bed_detail}
    return render(request, "plants/bed_detail.html", context=context)


# class BedDetailView(DetailView):
#     model = Planting
#     template_name = "plants/bed_detail.html"
#     context_object_name = "bed_detail"


class PlantListView(ListView):
    model = Plant
    template_name = "plants/plant_list.html"


class PlantDetailView(DetailView):
    model = Plant
    template_name = "plants/plant_detail.html"


class JournalEntryListView(ListView):
    model = JournalEntry
    template_name = "plants/journalentry_list.html"


class JournalEntryDetailView(DetailView):
    model = JournalEntry
    template_name = "plants/journalentry_detail.html"


def index(request):
    return render(request, "plants/index.html")
