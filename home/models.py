from django.db import models

# Create your models here.


class AboutUser(models.Model):

    class Meta:
        verbose_name_plural = 'About the user'

    full_name = models.CharField(max_length=50)
    profession = models.CharField(max_length=50, null=True, blank=True)
    github_link = models.URLField(max_length=254, null=True, blank=True)
    facebook_link = models.URLField(max_length=254, null=True, blank=True)
    linkedin_link = models.URLField(max_length=254, null=True, blank=True)
    twitter_link = models.URLField(max_length=254, null=True, blank=True)
    about_entry_one = models.TextField(max_length=254)
    about_entry_two = models.TextField(max_length=254, null=True, blank=True)
    about_entry_three = models.TextField(max_length=254, null=True, blank=True)
    hero_image_url = models.URLField(max_length=1024, null=True, blank=True)
    hero_image = models.ImageField(null=True, blank=True)
    about_image_url = models.URLField(max_length=1024, null=True, blank=True)
    about_image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.full_name
