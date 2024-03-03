from django.db import models
from versatileimagefield.fields import VersatileImageField


class Plant(models.Model):
    class Meta:
        ordering = ["name", "variety"]

    name = models.CharField(max_length=250, null=False, blank=False)
    variety = models.CharField(max_length=250, null=False, blank=False)
    source = models.CharField(max_length=250, null=False, blank=False)
    link = models.URLField(blank=True, null=True)
    image = VersatileImageField(blank=True, null=True, width_field="img_width", height_field="img_height")
    img_width = models.IntegerField(blank=True, null=True, verbose_name="image width")
    img_height = models.IntegerField(blank=True, null=True, verbose_name="image height")
    min_germ_days = models.IntegerField(null=False, blank=False, verbose_name="min days to germinate")
    max_germ_days = models.IntegerField(null=False, blank=False, verbose_name="max days to germinate")
    min_maturity_days = models.IntegerField(null=False, blank=False, verbose_name="min days to maturity")
    max_maturity_days = models.IntegerField(null=False, blank=False, verbose_name="max days to maturity")
    first_start_dt = models.DateField(null=False, blank=False, verbose_name="earliest start date")
    last_start_dt = models.DateField(null=False, blank=False, verbose_name="latest start date")
    first_plant_dt = models.DateField(null=False, blank=False, verbose_name="earliest plant date")
    last_plant_dt = models.DateField(null=False, blank=False, verbose_name="latest plant date")

    def __str__(self):
        return f"{self.name} {self.variety}"


class Bed(models.Model):
    class Meta:
        ordering = ["num"]

    CHOICES = [(1, "1"),
               (2, "2"),
               (3, "3"),
               (4, "4"),
               (5, "5"),
               (6, "6"),
               (7, "7"),
               (8, "8"),
               (9, "9"),
               (0, "Starts")]

    num = models.SmallIntegerField(blank=False, null=False, verbose_name="bed number", choices=CHOICES)
    image = VersatileImageField(blank=True, null=True, width_field="img_width", height_field="img_height",
                                verbose_name="current image")
    img_width = models.IntegerField(blank=True, null=True, verbose_name="image width")
    img_height = models.IntegerField(blank=True, null=True, verbose_name="image height")
    is_raised = models.BooleanField(default=False, verbose_name="raised bed")

    def __str__(self):
        return f"{self.num}"


class Planting(models.Model):
    class Meta:
        ordering = ["bed", "plant"]

    bed = models.ForeignKey("Bed", on_delete=models.PROTECT)
    plant = models.ForeignKey("Plant", on_delete=models.PROTECT)
    row = models.IntegerField(blank=False, null=False)
    count = models.IntegerField(blank=False, null=False)
    start_dt = models.DateField(blank=False, null=False, verbose_name="date started")
    plant_dt = models.DateField(blank=True, null=True, verbose_name="date planted")
    harvest_dt = models.DateField(blank=True, null=True, verbose_name="date harvested")

    def __str__(self):
        return f"{self.bed}"


class JournalNote(models.Model):
    class Meta:
        ordering = ["-date"]
        verbose_name = "journal note"
        verbose_name_plural = "journal notes"

    date = models.DateTimeField(blank=False, null=False)
    task = models.ForeignKey("Task", blank=True, null=True, on_delete=models.PROTECT)
    bed = models.ForeignKey("Bed", blank=True, null=True, on_delete=models.PROTECT)
    note = models.TextField(blank=True, null=True)
    image = VersatileImageField(blank=True, null=True)
    image_desc = models.CharField(max_length=250, blank=True, null=True)

    def __str__(self):
        return f"{self.date}"

    def get_queryset(self):
        journalnote_list = JournalNote.objects.order_by("date").filter(":5")
        return journalnote_list


class Task(models.Model):
    INTERVALS = {"DAILY": "Daily",
                 "WEEKLY": "Weekly",
                 "MONTHLY": "Monthly",
                 "YEARLY": "Yearly"}
    task = models.CharField(max_length=255, null=False, blank=False)—
    period = models.CharField(max_length=255, null=True, blank=True, choices=INTERVALS, verbose_name="period")
    count = models.IntegerField(null=True, blank=True, default=0, verbose_name="iterations per period)")
    start = models.DateField(null=True, blank=True)
    end = models.DateField(null=True, blank=True)
    note = models.TextField(null=True, blank=True)

    class Meta:
        ordering = ["task"]

    def __str__(self):
        return f"{self.task}"
