from django.db import models

# Create your models here.
from django.utils.crypto import get_random_string

class URL(models.Model):
    original_url = models.URLField(unique=True)
    short_code = models.CharField(max_length=6, unique=True, blank=True)
    click_count = models.IntegerField(default=0)

    def save(self, *args, **kwargs):
        if not self.short_code:
            self.short_code = get_random_string(length=6)
        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.original_url} -> {self.short_code} ({self.click_count} clicks)'