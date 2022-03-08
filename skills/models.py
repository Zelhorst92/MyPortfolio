from django.db import models

# Create your models here.


class Skill(models.Model):
    name = models.CharField(max_length=254)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    hidden = models.BooleanField(default=False)

    def __str__(self):
        return self.name
