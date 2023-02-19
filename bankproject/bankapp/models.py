from django.db import models


# Create your models here.


class District(models.Model):
    district = models.CharField(max_length=250)
    wiki = models.URLField(max_length=200)

    class Meta:
        ordering = ('district',)

    def __str__(self):
        return '{}'.format(self.district)


class Branch(models.Model):
    district = models.ForeignKey(District, on_delete=models.CASCADE)
    branch = models.CharField(max_length=250)


    class Meta:
        ordering = ('district',)

    def __str__(self):
        return '{}'.format(self.branch)
