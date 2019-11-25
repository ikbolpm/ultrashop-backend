from django.db import models

# Create your models here.
class Deal(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to='deal_images')
    url = models.CharField(max_length=300)
    active = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return self.name

