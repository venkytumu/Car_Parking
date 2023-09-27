from django.db import models

class Slot(models.Model):
    booking_date=models.DateField(default='2023-01-01')
    slot_number = models.IntegerField()
    is_selected = models.BooleanField(default=False)
    is_available = models.BooleanField(default=True)

class Booking(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    slot = models.ForeignKey(Slot, on_delete=models.CASCADE)
    booking_date = models.DateTimeField(auto_now_add=True)
