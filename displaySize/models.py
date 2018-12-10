from django.db import models

class DisplaySize(models.Model):
    size = models.CharField(max_length=40, unique=True)

    class Meta:
        ordering = ['size']

    def __str__(self):
        return self.size