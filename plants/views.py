from django.shortcuts import render
from django.views.generic import DetailView, ListView
from .models import Bed, JournalEntry, Plant, Planting, Task


class BedListView(ListView):
    model = Bed
    template_name = "plants/bed_list.html"


def bed_detail_view(request, bed):
    plantings = Planting.objects.filter(bed__bed=bed)
    is_raised = Bed.objects.get(bed=bed).is_raised
    context = {'bed': bed, 'is_raised': is_raised, 'plantings': plantings}
    return render(request, "plants/bed_detail.html", context=context)


# class BedDetailView(DetailView):
#     model = Planting
#     template_name = "plants/bed_detail.html"
#     context_object_name = "bed_detail"
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         return context


def index(request):
    views = ["beds", "plants", "tasks", "journal"]
    return render(request, 'plants/index.html', context={"views": views})


class JournalEntryListView(ListView):
    model = JournalEntry
    template_name = "plants/journalentry_list.html"


class JournalEntryDetailView(DetailView):
    model = JournalEntry
    template_name = "plants/journalentry_detail.html"


class PlantListView(ListView):
    model = Plant
    template_name = "plants/plant_list.html"


class PlantDetailView(DetailView):
    model = Plant
    template_name = "plants/plant_detail.html"


class TaskListView(ListView):
    model = Task
    template_name = "plants/task_list.html"

    def get_queryset(self):
        return Task.objects.all()


class TaskDetailView(DetailView):
    model = Task
    template_name = "plants/task_detail.html"
