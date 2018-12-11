from django.db import models

from laptop.models import Laptop


class Lead(models.Model):
    STATUS_CHOICES = (
        ('NOT_CONTACTED', 'Not Contacted'),
        ('ATTEMPTED_TO_CONTACT', 'Attempted to Contact'),
        ('ASKED_TO_CALL_LATER', 'Asked to Call Later'),
        ('DECISION_MAKING', 'Decision Making'),
        ('CLOSED_WON', 'Closed Won'),
        ('CLOSED LOST', 'Closed Lost')
    )
    name = models.CharField(max_length=200)
    phone_or_im = models.CharField(max_length=200)
    description = models.TextField()
    status = models.CharField(choices=STATUS_CHOICES, default='NOT_CONTACTED', max_length=30)
    amount = models.IntegerField(blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateField(auto_now=True)

    class Meta:
        unique_together = ['name', 'phone_or_im']

    def __str__(self):
        return self.name