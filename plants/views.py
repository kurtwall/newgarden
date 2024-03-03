from django.shortcuts import render
from django.views.generic import DetailView, ListView

from .models import Bed, JournalNote, Plant, Planting, Task


# The landing page
def index(request):
    views = ["beds", "plants", "tasks", "journal"]
    return render(request, 'plants/index.html', context={"views": views})


class BedListView(ListView):
    model = Bed
    template_name = "plants/bed_list.html"


def bed_detail_view(request, num):
    plantings = Planting.objects.filter(bed__num=num)
    is_raised = Bed.objects.get(num=num).is_raised
    context = {'num': num, 'is_raised': is_raised, 'plantings': plantings}
    return render(request, "plants/bed_detail.html", context=context)


class JournalNoteListView(ListView):
    model = JournalNote
    template_name = "plants/journal_note_list.html"


class JournalNoteDetailView(DetailView):
    model = JournalNote
    template_name = "plants/journal_note_detail.html"


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
