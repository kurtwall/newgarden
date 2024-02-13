from django.contrib import admin

from plants.models import Bed, JournalEntry, Plant, Planting, Task

admin.site.register(Bed)
admin.site.register(JournalEntry)
admin.site.register(Plant)
admin.site.register(Planting)
admin.site.register(Task)
