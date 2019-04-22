from django.db import models
from commits.models import Commit


class CommitDay(models.Model):
    date = models.DateField(default=None)
    quantity = models.IntegerField()
    commit = models.ForeignKey(Commit, on_delete=models.CASCADE)
