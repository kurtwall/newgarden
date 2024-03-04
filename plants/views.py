from django.http import JsonResponse
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


# # TODO: This view might be unnecessary
# class TaskDetailView(DetailView):
#     model = Task
#     template_name = "plants/task_detail.html"
#
#
# View functions for FullCalendar. These views link FullCalendar's
# Javascript to Django's Python
def calendar(request):
    events = Task.objects.all()
    task_list = TaskListView.get_queryset(request)
    context = {
        "events": events,
        "task_list": task_list
    }
    return render(request, 'plants/calendar.html', context)


# "Events" here are instances of the Task model. They default to "all-day"
# durations. The view maps the Django model data (say, event.days_of_week)
# to the Javascript properties of the FullCalendar widget (daysOfWeek, in
# this case). The widget is expecting certain property names, so populate
# them from the queryset.
def all_events(request):
    all_events = Task.objects.all()
    out = []
    for event in all_events:
        if event.is_recurring:
            out.append({
                'title': event.name,
                'id': event.id,
                'allDay': True,
                'daysOfWeek': event.days_of_week,
                'startRecur': event.start_recur,
                'endRecur': event.end_recur
            })
        else:
            out.append({
                'title': event.name,
                'id': event.id,
                'allDay': True,
                'start': event.start,
                'end': event.end,
            })
    return JsonResponse(out, safe=False)


def add_event(request):
    start = request.GET.get("start", None)
    end = request.GET.get("end", None)
    title = request.GET.get("title", None)
    event = Events(name=str(title), start=start, end=end)
    event.save()
    data = {}
    return JsonResponse(data, safe=False)


def update(request):
    start = request.GET.get("start", None)
    end = request.GET.get("end", None)
    title = request.GET.get("title", None)
    id = request.GET.get("id", None)
    event = Events.objects.get(id=id)
    event.start = start
    event.end = end
    event.name = title
    event.save()
    data = {}
    return JsonResponse(data, safe=False)


def remove(request):
    id = request.GET.get("id", None)
    event = Events.objects.get(id=id)
    event.delete()
    data = {}
    return JsonResponse(data, safe=False)
