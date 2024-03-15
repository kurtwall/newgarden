from django.urls import path

from plants import views
from .views import calendar, all_events

urlpatterns = (([
    path("", views.index, name="index"),
    path("beds/", views.BedListView.as_view(), name="bed_list"),
    path("beds/<num>/", views.bed_detail_view, name="bed_detail"),
    path("journal/", views.JournalNoteListView.as_view(), name="journalnote_list"),
    path("journal/<int:pk>/", views.JournalNoteDetailView.as_view(), name="journalnote_detail"),
    path("journal/add/", views.JournalCreateNoteView.as_view(), name="journalnote_create"),
    path("journal/update/<int:pk>/", views.JournalUpdateNoteView.as_view(), name="journalnote_edit"),
    path("journal/delete/<int:pk>/", views.JournalDeleteNoteView.as_view(), name="journalnote_delete"),
    path("plants/", views.PlantListView.as_view(), name="plant_list"),
    path("plants/<int:pk>/", views.PlantDetailView.as_view(), name="plant_detail"),
    path('tasks/', calendar, name='calendar'),
    path("tasks/<int:pk>/", views.TaskDetailView.as_view(), name="task_detail"),
    path("tasks/add/", views.TaskCreateView.as_view(), name="task_add"),
    path("tasks/update/<int:pk>", views.TaskUpdateView.as_view(), name="task_edit"),
    path("tasks/delete/<int:pk>/", views.TaskDeleteView.as_view(), name="task_delete"),
    path('all_events/', all_events, name='all_events'),
]))
