from django.db import models

# Create your models here.


class PreviousProject(models.Model):

    class Meta:
        verbose_name_plural = 'Previous Project Items'

    name = models.CharField(max_length=254)
    description = models.TextField(max_length=1024, null=True, blank=True)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name


class AboutUser(models.Model):
    full_name = models.CharField(max_length=50)
    profession = models.CharField(max_length=50, null=True, blank=True)
    github_link = models.URLField(max_length=254, null=True, blank=True)
    facebook_link = models.URLField(max_length=254, null=True, blank=True)
    linkedin_link = models.URLField(max_length=254, null=True, blank=True)
    twitter_link = models.URLField(max_length=254, null=True, blank=True)
    about_entry_one = models.CharField(max_length=254, null=True, blank=True)
    about_entry_two = models.CharField(max_length=254, null=True, blank=True)
    about_entry_three = models.CharField(max_length=254, null=True, blank=True)
    hero_image_url = models.URLField(max_length=1024, null=True, blank=True)
    hero_image = models.ImageField(null=True, blank=True)
    about_image_url = models.URLField(max_length=1024, null=True, blank=True)
    about_image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.full_name
