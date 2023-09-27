from django.db import models
from django.contrib.auth.models import User

class Slot(models.Model):
    
    slot_number = models.IntegerField()

    is_selected = models.BooleanField(default=False)
    is_available = models.BooleanField(default=True)
    booking_date = models.DateField()
     

class Booking(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    slot = models.ForeignKey(Slot, on_delete=models.CASCADE)
    booking_date = models.DateTimeField(auto_now_add=True)
    #status = models.CharField(max_length=10, choices=[('pending', 'Pending'), ('confirmed', 'Confirmed'), ('declined', 'Declined')])

class HistoricalBooking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    slot = models.ForeignKey(Slot, on_delete=models.CASCADE)
    # booking_date = models.DateTimeField(auto_now_add=True)
    # booking1 = models.ForeignKey(Booking, on_delete=models.CASCADE)
    # booking_date = models.OneToOneField(Booking, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    # history_date = models.DateField()

    # def save(self, *args, **kwargs):
        
    #     if not self.history_date:
    #         self.history_date = self.booking1.booking_date.date() if self.booking1 else None # Set it to the booking date
    #     super(HistoricalBooking, self).save(*args, **kwargs)

