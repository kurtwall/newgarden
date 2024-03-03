from django.http import JsonResponse
from django.shortcuts import render
from django.views.generic import DetailView, ListView

from .models import Bed, JournalNote, Plant, Planting, Task, Events


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


# View functions for FullCalendar. These views link FullCalendar's
# Javascript to Django's Python
def calendar(request):
    events = Task.objects.all()
    context = {
        "events": events.all()
    }
    return render(request, 'plants/calendar.html', context)


# "Events" here are instances of the Task model. They default to "all-day"
# durations
def all_events(request):
    all_events = Task.objects.all()
    out = []
    for event in all_events:
        if event.start and event.end:
            out.append({
                'title': event.name,
                'id': event.id,
                'start': event.start,
                'end': event.end,
            })
    return JsonResponse(out, safe=False)

# def all_events(request):
#     all_events = Events.objects.all()
#     out = []
#     for event in all_events:
#         out.append({
#             'title': event.name,
#             'id': event.id,
#             'start': event.start.strftime("%m/%d/%Y, %H:%M:%S"),
#             'end': event.end.strftime("%m/%d/%Y, %H:%M:%S"),
#         })
#
#     return JsonResponse(out, safe=False)


def add_event(request):
    start = request.GET.get("start", None)
    end = request.GET.get("end", None)
    title = request.GET.get("title", None)
    event = Events(name=str(title), start=start, end=end)
    event.save()
    data = {}
    return JsonResponse(data)


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
    return JsonResponse(data)


def remove(request):
    id = request.GET.get("id", None)
    event = Events.objects.get(id=id)
    event.delete()
    data = {}
    return JsonResponse(data)
