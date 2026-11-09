from django.db import models
from django.db.models import Q, F
from django.contrib.auth import get_user_model

# Create your models here.
class Resource(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return self.name

class Reservation(models.Model):
    
    class Meta:
        constraints = [
            models.CheckConstraint(
                condition=Q(final_date__gt=F('initial_date')),
                name='valid_date_range'
            )
        ]

    user = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        related_name='reservations'
    ),
    resource = models.ForeignKey(
        Resource,
        on_delete=models.CASCADE,
        related_name='reservations',
    ),
    initial_date = models.DateTimeField()
    final_date = models.DateTimeField()
    
    def __str__(self):
        return f"{self.user} - {self.resource} - {self.initial_date} - {self.final_date}"
   
