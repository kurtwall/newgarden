# Gardener

A small garden journal built using the [Django framework](https://www.djangoproject.com/). It is mostly a
toy I wrote to salve my gardening jones and engage my brain during the dreary winter months when the
garden is (_mostly_) moribund. I find it useful for keeping track of garden activities, feeding and
watering schedules, and what is planted, where, and when I planted it.

It keeps track of your beds, the plants in them, and expected harvest dates. Gardener also provides a
calendaring/reminder function to provide a list of gardening chores that need to be completed, such as weeding,
watering, fertilizing, weeding suckering, weeding, and weeding. Finally, Gardener's journal feature enables you to
record events, notes, and activities about your garden in a journal.

## What is working

- Adding beds, plants, plantings, journal entries via the admin interface
- Bed, plant, planting, and journal entry list and detail views

## What is not working (in no particular order)

- [Scheduling/Reminders](https://django-recurrence.readthedocs.io/en/latest/index.html): Currently using
  django-recurrence
- [General styling](https://getbootstrap.com)
- Add CRUD views
- [Add a few useful charts](git@github.com:RamezIssac/django-slick-reporting.git)
- [Table styling](git@github.com:jieter/django-tables2.git)
- Switch to PostgreSQL?
- 