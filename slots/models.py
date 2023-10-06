from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Slot(models.Model):
    
    slot_number = models.IntegerField()
    is_selected = models.BooleanField(default=False)
    is_available = models.BooleanField(default=True)
    booking_date = models.DateField(default=timezone.now)

# def __str__(self):
#         return f"Slot {self.slot_number}"
# slot_instance = Slot(slot_number=10, is_selected=True, is_available=False)
# slot_instance.save()

class meta:
    verbose_name_plural = "Slot Details"

     

class Booking(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    slot = models.ForeignKey(Slot, on_delete=models.CASCADE)
    booking_date = models.DateTimeField(auto_now_add=True)

   
class HistoricalBooking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    slot = models.ForeignKey(Slot, on_delete=models.CASCADE) 
    created_at = models.DateTimeField(auto_now_add=True)
    

