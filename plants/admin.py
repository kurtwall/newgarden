from django.contrib import admin

from plants.models import Bed, JournalEntry, Plant, Planting

admin.site.register(Bed)
admin.site.register(JournalEntry)
admin.site.register(Plant)
admin.site.register(Planting)
