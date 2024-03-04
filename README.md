# Gardener

A small garden journal built using
the [Django framework](https://www.djangoproject.com/). It is mostly a
toy I wrote to salve my gardening jones and engage my brain during the dreary
winter
months when the
garden is mostly moribund. I find it useful for keeping track of garden
activities, feeding and
watering schedules, and what is planted, where, and when I planted it.

It keeps track of your beds, the plants in them, and expected harvest dates.
Gardener also provides a
calendaring/reminder function to provide a list of gardening chores that need to
be completed, such as weeding,
watering, fertilizing, weeding suckering, weeding, and weeding. Finally,
Gardener's journal feature enables you to
record events, notes, and activities about your garden in a journal.

## What is working

- Adding beds, plants, plantings, journal entries via the admin interface
- Bed, plant, planting, and journal entry list and detail views
- You can use the admin interface to add tasks, either singleton or repeating, and they will display in a calndar.
- 

## What is not working (in no particular order)

- Make a calendar of garden events and tasks
- Add, edit, delete journal notes
- Add, edit, delete plants -- delete sets a deleted flag
- Create daily/weekly worklists
- Create harvest date projections
- Relate journal entries to tasks, beds, plants
  - Support adding photos for journal entries, so need to relate journal notes to beds/plants
  - Show bed-related journal entries in the bed detail view, again noting the need to relate journal notes to beds/plants
  - Show plant-related journal entries in the plant detail view, again noting the need to relate journal notes to beds/plants
- Ability to record actual harvest results for a given plant or planting
- Support tags for searching journal entries
- [Add a few useful charts](git@github.com:RamezIssac/django-slick-reporting.git)
- [General styling](https://getbootstrap.com)
- [Table styling](git@github.com:jieter/django-tables2.git)
- Replace stock bed images with actual images
- 
