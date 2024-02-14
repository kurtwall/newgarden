# Gardener

A small garden journal based on the [Django frankwork](https://www.djangoproject.com/). It is mostly a toy I wrote to
amuse myself during the dreary winter months when the garden is (_mostly_) idle.

It keeps track of your beds, the plants in them, and expected harvest dates. Gardener also provides a
calendaring/reminder function to provide a list of gardening chores that need to be completed, such as weeding,
watering, fertilizing, weeding suckering, weeding, and weeding. Finally, Gardener's journal feature enables you to
record events, notes, and activities about your garden in a journal.

## What's Working

- Adding beds, plants, plantings, journal entries via the admin interface
- Bed, plant, planting, and journal entry list and detail views

## TODO (in no particular order)

- [Add a few useful charts](git@github.com:RamezIssac/django-slick-reporting.git)
- [Table styling](git@github.com:jieter/django-tables2.git)
- [Scheduling/Reminders](https://django-recurrence.readthedocs.io/en/latest/index.html)
- Add CRUD views
- Switch to PostgreSQL?