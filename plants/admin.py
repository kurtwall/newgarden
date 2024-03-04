from django.contrib import admin

from plants.models import Bed, JournalNote, Plant, Planting, Task


class JournalEntryAdmin(admin.ModelAdmin):
    list_display = ["date", "task", "note"]


class PlantAdmin(admin.ModelAdmin):
    list_display = ["name", "variety", "source"]


class PlantingAdmin(admin.ModelAdmin):
    list_display = ["bed", "plant", "count", "start_dt"]


class TaskAdmin(admin.ModelAdmin):
    list_display = ["name", "note", "start", "end", "is_recurring", "start_recur", "end_recur", "days_of_week"]


admin.site.register(Bed)
admin.site.register(JournalNote, JournalEntryAdmin)
admin.site.register(Plant, PlantAdmin)
admin.site.register(Planting, PlantingAdmin)
admin.site.register(Task, TaskAdmin)
