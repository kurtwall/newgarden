from django.contrib import admin

from plants.models import Bed, JournalEntry, Plant, Planting, Task


class JournalEntryAdmin(admin.ModelAdmin):
    list_display = ["date", "task", "entry"]


class PlantAdmin(admin.ModelAdmin):
    list_display = ["name", "variety", "source"]


class PlantingAdmin(admin.ModelAdmin):
    list_display = ["bed", "plant", "count", "start_dt"]


class TaskAdmin(admin.ModelAdmin):
    list_display = ["task", "freq", "note"]


admin.site.register(Bed)
admin.site.register(JournalEntry, JournalEntryAdmin)
admin.site.register(Plant, PlantAdmin)
admin.site.register(Planting, PlantingAdmin)
admin.site.register(Task, TaskAdmin)
