from django.db import models

class Race(models.Model):
    designation=models.CharField(max_length=255)
    def __str__(self):
        return self.designation