from django.db import models

class DisplaySize(models.Model):
    size = models.CharField(max_length=40)

    def __str__(self):
        return self.size