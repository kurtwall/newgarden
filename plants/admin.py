from django.contrib import admin

from plants.models import Bed, Events, JournalNote, Plant, Planting, Task


class JournalEntryAdmin(admin.ModelAdmin):
    list_display = ["date", "task", "note"]


class PlantAdmin(admin.ModelAdmin):
    list_display = ["name", "variety", "source"]


class PlantingAdmin(admin.ModelAdmin):
    list_display = ["bed", "plant", "count", "start_dt"]


class TaskAdmin(admin.ModelAdmin):
    list_display = ["name", "period", "count", "note"]


class EventsAdmin(admin.ModelAdmin):
    list_display = ["name", "start", "end"]


admin.site.register(Bed)
admin.site.register(Events, EventsAdmin)
admin.site.register(JournalNote, JournalEntryAdmin)
admin.site.register(Plant, PlantAdmin)
admin.site.register(Planting, PlantingAdmin)
admin.site.register(Task, TaskAdmin)
