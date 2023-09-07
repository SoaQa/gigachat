from django.db import models
from django.urls import reverse


class UserProfile(models.Model):
    email = models.EmailField(max_length=255, unique=True)
    password = models.CharField(max_length=128, null=True, blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.email

    def get_absolute_url(self):
        return reverse('profile_detail', args=[str(self.id)])
