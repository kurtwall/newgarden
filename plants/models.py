from django.db import models


class Bed(models.Model):
    bed = models.IntegerField(blank=False, null=False, unique=True, verbose_name="bed number")
    is_raised = models.BooleanField(default=False, verbose_name="raised bed")

    def __str__(self):
        return f"{self.bed}"


class Plant(models.Model):

    class Meta:
        ordering = ["name", "variety"]

    name = models.CharField(max_length=250, null=False, blank=False)
    variety = models.CharField(max_length=250, null=False, blank=False)
    source = models.CharField(max_length=250, null=False, blank=False)
    link = models.URLField(blank=True, null=True)
    image = models.ImageField(blank=True, null=True, width_field="img_width", height_field="img_height")
    img_width = models.IntegerField(blank=True, null=True, verbose_name="image width")
    img_height = models.IntegerField(blank=True, null=True, verbose_name="image height")
    min_germ_days = models.IntegerField(null=False, blank=False, verbose_name="minimum days to germinate")
    max_germ_days = models.IntegerField(null=False, blank=False, verbose_name="maximum days to germinate")
    min_maturity_days = models.IntegerField(null=False, blank=False, verbose_name="minimum days to maturity")
    max_maturity_days = models.IntegerField(null=False, blank=False, verbose_name="maximum days to maturity")
    first_start_dt = models.DateField(null=False, blank=False, verbose_name="earliest start date")
    last_start_dt = models.DateField(null=False, blank=False, verbose_name="latest start date")
    first_plant_dt = models.DateField(null=False, blank=False, verbose_name="earliest plant date")
    last_plant_dt = models.DateField(null=False, blank=False, verbose_name="latest plant date")
    date_added = models.DateField(auto_now_add=True, verbose_name="date added")
    last_updated = models.DateField(auto_now=True, verbose_name="last updated")

    def __str__(self):
        return f"{self.name} {self.variety}"


class Planting(models.Model):

    class Meta:
        ordering = ["bed", "plant"]

    bed = models.ForeignKey(Bed, on_delete=models.CASCADE)
    plant = models.ForeignKey(Plant, on_delete=models.CASCADE)
    row = models.IntegerField(blank=False, null=False)
    count = models.IntegerField(blank=False, null=False)
    start_dt = models.DateField(blank=False, null=False)
    plant_dt = models.DateField(blank=False, null=False)
    harvest_dt = models.DateField(blank=False, null=False)

    def __str__(self):
        return f"B{self.bed}-R{self.row} {self.count} {self.plant.name}"


class Task(models.Model):
    TASKS = [(0, "start"), (1, "plant"), (2, "weed"), (3, "water"), (4, "fertilize"), (5, "sucker"), (6, "deadhead"),
             (7, "pot up"), (100, "other")]
    FREQS = [("d", "daily"), ("w", "weekly"), ("m", "monthly"), ("y", "yearly")]
    task = models.IntegerField(blank=False, null=False, choices=TASKS)
    freq = models.CharField(max_length=1, blank=False, null=False, verbose_name="frequency", choices=FREQS)
    note = models.CharField(max_length=250, blank=True, null=True)

    def __str__(self):
        return f"{self.task}"


class JournalEntry(models.Model):
    date = models.DateField(blank=False, null=False, auto_now_add=True)
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    entry = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.date}: {self.task}"
