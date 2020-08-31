from django.db import models

class VerbModel(models.Model):
    verbClass = models.CharField(max_length = 10)
    verbs = models.TextField()