from django.http import JsonResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView

from plants.models import Bed, JournalNote, Plant, Planting, Task


# The landing page
def index(request):
    views = ["beds", "plants", "calendar", "journal"]
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
    template_name = "plants/journalnote_list.html"


class JournalNoteDetailView(DetailView):
    model = JournalNote
    template_name = "plants/journalnote_detail.html"


class PlantListView(ListView):
    model = Plant
    template_name = "plants/plant_list.html"


class JournalCreateNoteView(CreateView):
    model = JournalNote
    fields = ["date", "task", "bed", "note", "image", "image_desc"]


class JournalUpdateNoteView(UpdateView):
    model = JournalNote
    fields = ["date", "task", "bed", "note", "image", "image_desc"]


class JournalDeleteNoteView(DeleteView):
    model = JournalNote
    success_url = reverse_lazy("journalnote_list")


class PlantDetailView(DetailView):
    model = Plant
    template_name = "plants/plant_detail.html"


class TaskDetailView(DetailView):
    model = Task
    template_name = "plants/task_detail.html"


class TaskCreateView(CreateView):
    model = Task
    fields = ["name", "note", "start", "end", "is_recurring", "start_recur", "end_recur", "days_of_week",
              "is_completed"]
    template_name = "plants/task_form.html"


class TaskUpdateView(UpdateView):
    model = Task
    fields = ["name", "note", "start", "end", "is_recurring", "start_recur", "end_recur", "days_of_week",
              "is_completed"]
    template_name = "plants/task_form.html"


class TaskDeleteView(DeleteView):
    model = Task
    success_url = reverse_lazy("all_events")


# View functions for FullCalendar. These views link FullCalendar's Javascript to Django's Python. FullCalendar's Event
# object maps roughly to the Task model, so an "event" is a "task". The view maps the Django model data (say, task.name)
# to the Javascript properties of the FullCalendar widget (event.title, in this case).
def calendar(request):
    events = Task.objects.all()
    context = {
        "events": events,
    }
    return render(request, 'plants/calendar.html', context)


# The calendar widget expects certain options and property names, so populate
# them from the queryset.
def all_events(request):
    tasks = Task.objects.all()
    out = []
    for task in tasks:
        if task.is_recurring:
            out.append({
                'title': task.name,
                'id': task.id,
                'allDay': True,
                'daysOfWeek': task.days_of_week,
                'startRecur': task.start_recur,
                'endRecur': task.end_recur,
                'url': task.get_absolute_url()
            })
        else:
            out.append({
                'title': task.name,
                'id': task.id,
                'allDay': True,
                'start': task.start,
                'end': task.end,
                'url': task.get_absolute_url()
            })
    return JsonResponse(out, safe=False)
