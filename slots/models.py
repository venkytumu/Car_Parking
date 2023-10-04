from django.db import models
from django.contrib.auth.models import User

class Slot(models.Model):
    
    slot_number = models.IntegerField()
    is_selected = models.BooleanField(default=False)
    is_available = models.BooleanField(default=True)
    booking_date = models.DateField()
    shifts = models.IntegerField()
     

class Booking(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    slot = models.ForeignKey(Slot, on_delete=models.CASCADE)
    booking_date = models.DateTimeField(auto_now_add=True)
   
class HistoricalBooking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    slot = models.ForeignKey(Slot, on_delete=models.CASCADE) 
    created_at = models.DateTimeField(auto_now_add=True)
    

