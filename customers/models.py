from django.db import models

from laptop.models import Laptop


class Customer(models.Model):
    name = models.CharField(max_length=255, help_text='Полное имя покупателя. Например: Кобулов Икбол')
    phone = models.CharField(max_length=15, help_text='Номер телефона покупателя в формате 998 91 192 2228')
    email = models.EmailField(blank=True, null=True)
    created = models.DateField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['name']
        unique_together = ['name', 'phone']

    def __str__(self):
        return self.name
