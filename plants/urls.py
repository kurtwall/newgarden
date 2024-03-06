from django.urls import path

from plants import views
from .views import calendar, add_event, update, remove, all_events

urlpatterns = (([
    path("", views.index, name="index"),
    path("beds/", views.BedListView.as_view(), name="bed_list"),
    path("beds/<num>/", views.bed_detail_view, name="bed_detail"),
    path("journal/", views.JournalNoteListView.as_view(), name="journal_note_list"),
    path("journal/<int:pk>/", views.JournalNoteDetailView.as_view(), name="journalentry_detail"),
    path("plants/", views.PlantListView.as_view(), name="plant_list"),
    path("plants/<int:pk>/", views.PlantDetailView.as_view(), name="plant_detail"),
    path('tasks/', calendar, name='calendar'),
    path("tasks/", views.TaskListView.as_view(), name="task_list"),
    path("tasks/add/", views.AddTaskView.as_view(), name="add_task"),
    path("tasks/<int:pk>/", views.TaskDetailView.as_view(), name="task_detail"),
    # path('add_event/', views.AddTaskView.as_view(), name='add_event'),
    # path('update/', update, name='update'),
    # path('remove/', remove, name='remove'),
    path('all_events/', all_events, name='all_events'),
]))



