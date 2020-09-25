from django.db import models

# Create your models here.
class Country(models.Model):
    country = models.CharField(max_length=5)
    year = models.CharField(max_length=20)

    def __str__(self):
        return self.country

    class Meta:
        verbose_name_plural = 'countries'

class Holiday(models.Model):
    holiday = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    date = models.CharField(max_length=50)
    location = models.CharField(max_length=50)
    states = models.CharField(max_length=50)
    _type = models.CharField(max_length=100, null=True, blank=True)
    country = models.ForeignKey(to=Country, on_delete=models.CASCADE)

    def __str__(self):
        return self.holiday

    class Meta:
        verbose_name_plural = 'holidays'