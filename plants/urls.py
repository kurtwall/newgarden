from django.urls import path

from plants import views
from .views import calendar, add_event, all_events, remove_event, update_event

urlpatterns = (([
    path("", views.index, name="index"),
    path("beds/", views.BedListView.as_view(), name="bed_list"),
    path("beds/<num>/", views.bed_detail_view, name="bed_detail"),
    path("journal/", views.JournalNoteListView.as_view(), name="journal_note_list"),
    path("journal/<int:pk>/", views.JournalNoteDetailView.as_view(), name="journalentry_detail"),
    path("plants/", views.PlantListView.as_view(), name="plant_list"),
    path("plants/<int:pk>/", views.PlantDetailView.as_view(), name="plant_detail"),
    path('tasks/', calendar, name='calendar'),
    path("tasks/<int:pk>/", views.TaskDetailView.as_view(), name="task_detail"),
    path('all_events/', all_events, name='all_events'),
    path('add_event/', add_event, name='add_event'),
    path('update_event/', update_event, name='update_event'),
    path('remove_event/', remove_event, name='remove_event'),
]))
