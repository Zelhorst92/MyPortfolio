from django.db import models

# Create your models here.

class Project(models.Model):

    class Meta:
        verbose_name_plural = 'Previous Projects'

    name = models.CharField(max_length=254)
    description = models.TextField(max_length=1024, null=True, blank=True)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    github_link = models.URLField(null=True, blank=True)
    site_link = models.URLField(null=True, blank=True)
    hidden = models.BooleanField(default=False)

    def __str__(self):
        return self.name
