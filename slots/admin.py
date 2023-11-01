from django.contrib import admin

from .models import Slot, Booking, HistoricalBooking

from django.shortcuts import HttpResponseRedirect

from import_export.admin import ImportExportModelAdmin

from django.contrib.auth.models import User  # Replace with your custom user model if applicable

from .models import Notification
from django.contrib.auth.models import User
# from django.contrib.auth.models import UserAdmin

 

admin.site.site_header = 'Admin Panel'


# class UserAdmin(ImportExportModelAdmin):

#     list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff', 'date_joined')

#     ordering = ('-date_joined',)  # Reverse order by date joined

# # admin.site.unregister(User)  # Unregister the default User admin

# admin.site.register(User, UserAdmin)  # Register the User admin with import/export capabilities

 

class SlotAdmin(admin.ModelAdmin):

    list_display = ('slot_number', 'is_available', 'is_selected', 'booking_date', 'shifts')

    ordering = ('booking_date', 'shifts', 'slot_number')

    list_filter = ('booking_date', 'is_available', 'is_selected', 'slot_number', 'shifts')

    actions = ['book_selected_slots', 'release_selected_slots']

    # date_hierarchy= 'booking_date'

    list_per_page = 20

 

    def book_selected_slots(self, request, queryset):

        user = request.user  # Get the current admin user

        # Loop through selected slots and create booking records for the user

        for slot in queryset:

            Booking.objects.create(slot=slot, user=user, slot_number=slot.slot_number, shifts=slot.shifts,booking_date=slot.booking_date)

            # Update the selected slots to be booked

            slot.is_selected = False

            slot.is_available = False

            slot.save()


    book_selected_slots.short_description = "Book selected slots"

    def release_selected_slots(self, request, queryset):

        slot_ids = queryset.values_list('id', flat=True)
        queryset.update(is_selected=False, is_available=True)
        Booking.objects.filter(slot_id__in=slot_ids).delete()
        users=User.objects.all()
        for user in users:
            for slot in queryset:
                message = f"Admin has released slot On {slot.booking_date}, slot number {slot.slot_number} and shift number {slot.shifts} and is now available for booking.."
                Notification.objects.create(recipient=user, message=message)

    book_selected_slots.short_description = "Book selected slots"

    release_selected_slots.short_description = "Release selected slots"

admin.site.register(Slot, SlotAdmin)

class BookingAdmin(admin.ModelAdmin):
    list_display = ('user', 'slot_number', 'booking_date', 'shifts')
    ordering = ('slot_number', 'booking_date')
    list_filter = ('user', 'slot_number', 'booking_date', 'shifts')
    def book_selected_slots(self, request, queryset):
        for slot in queryset:
            Booking.objects.create(slot=slot, user=request.user, slot_number=slot.slot_number, shifts=slot.shifts,booking_date=slot.booking_date)
        queryset.update(is_selected=False, is_available=False)
    book_selected_slots.short_description = "Book selected slots"
admin.site.register(Booking, BookingAdmin)

class HistoricalBookingAdmin(ImportExportModelAdmin):

    list_display = ('user', 'slot_number', 'shifts', 'booking_date', 'created_at')

    ordering = ('created_at', 'slot_id')

    list_filter = ('user', 'slot_number', 'booking_date', 'shifts')

 

admin.site.register(HistoricalBooking, HistoricalBookingAdmin)
# @admin.action(description="Release selected slots")
# def release_selected_slots(self, request, queryset):
#     released_slot_ids = []
#     for slot in queryset:
#         # Mark the slot as available
#         slot.is_available = True
#         slot.save()
 
#         # Create a notification for all users
#         users = User.objects.all()
#         for user in users:
#             message = f"Admin has released slot {slot.slot_number}."
#             Notification.objects.create(recipient=user, message=message)
#             released_slot_ids.append(slot.slot_number)
 
#     # Notify all users about the released slots
#     self.message_user(
#         request, f"{len(queryset)} slots released and notified to users: {', '.join(map(str, released_slot_ids))}"
#     )