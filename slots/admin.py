from django.contrib import admin
from django.utils import timezone
from .models import Slot, Booking, HistoricalBooking

admin.site.site_header = 'Admin Panel'

class SlotAdmin(admin.ModelAdmin):
    list_display = ('slot_number', 'is_available', 'is_selected', 'booking_date')
    ordering = ('booking_date', 'slot_number')
    list_filter = ('slot_number', 'is_available', 'is_selected', 'booking_date')
    actions = ['book_selected_slots', 'release_selected_slots']
    list_per_page=10

    def book_selected_slots(self, request, queryset):
        # Update the selected slots to be booked
        queryset.update(is_selected=False, is_available=False)

    def release_selected_slots(self, request, queryset):
        # Update the selected slots to be released
        queryset.update(is_selected=False, is_available=True)

    book_selected_slots.short_description = "Book selected slots"
    release_selected_slots.short_description = "Release selected slots"

admin.site.register(Slot, SlotAdmin)

class BookingAdmin(admin.ModelAdmin):
    list_display=('user','slot','booking_date')
    ordering=('slot','booking_date')
    list_filter=('user','slot','booking_date')

def book_selected_slots(self, request, queryset):
    # Loop through selected slots and create booking records
    for slot in queryset:
        Booking.objects.create(slot=slot, user=request.user)  # Modify as needed

    # Update the selected slots to be booked
    queryset.update(is_selected=False, is_available=False)
    
admin.site.register(Booking, BookingAdmin)

class HistoricalBookingAdmin(admin.ModelAdmin):
    list_display=('created_at','slot_id','user_id')
    ordering=('created_at','slot_id')
    
    # def save_model(self, request, obj, form, change):
    #     # Automatically update is_available and is_selected fields
    #     if obj.is_selected:
    #         obj.is_available = False
    #     else:
    #         obj.is_available = True
    #     super().save_model(request, obj, form, change)



# admin.site.register(Booking)
admin.site.register(HistoricalBooking,HistoricalBookingAdmin)
