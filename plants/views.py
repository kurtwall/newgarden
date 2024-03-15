from django.http import JsonResponse
from django.shortcuts import render
from django.views.generic import DetailView, ListView

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


class TaskDetailView(DetailView):
    model = Task
    template_name = "plants/task_detail.html"


class AddTaskView():
    pass


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
                'url': task.get_absolute_url(),
                'extendedProps': {'fooproperty': 'barvalue'},
            })
        else:
            out.append({
                'title': task.name,
                'id': task.id,
                'allDay': True,
                'start': task.start,
                'end': task.end,
                'url': task.get_absolute_url(),
                'extendedProps': {'fooproperty': 'barvalue'},
            })
    return JsonResponse(out, safe=False)


def add_event(request):
    name = request.GET.get("name", None)
    is_recurring = request.GET.get("isRecurring")
    start = request.GET.get("start", None)
    end = request.GET.get("end", None)
    days_of_week = request.GET.get("daysOfWeek", None)
    start_recur = request.GET.get("startRecur", None)
    end_recur = request.GET.get("endRecur", None)
    all_day = True
    event = Task(name=str(name), start=start, end=end, allDay = all_day, is_recurring=is_recurring,
                 days_of_week=days_of_week, start_recur=start_recur, end_recur=end_recur)
    event.save()
    data = {}
    return JsonResponse(data, safe=False)


def update_event(request):
    start = request.GET.get("start", None)
    end = request.GET.get("end", None)
    title = request.GET.get("title", None)
    id = request.GET.get("id", None)
    event = Task.objects.get(id=id)
    event.start = start
    event.end = end
    event.name = title
    event.save()
    data = {}
    return JsonResponse(data, safe=False)


def remove_event(request):
    id = request.GET.get("id", None)
    task = Task.objects.get(id=id)
    task.delete()
    data = {}
    return JsonResponse(data, safe=False)
