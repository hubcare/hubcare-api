from django.db import models


class Readme(models.Model):
    owner = models.CharField(max_length=150)
    repo = models.CharField(max_length=150)
    readme = models.BooleanField(default=False)

    class Meta:
        unique_together = (('owner', 'repo'),)
