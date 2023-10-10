from django.shortcuts import render, redirect, HttpResponse
from .models import Slot, Booking,HistoricalBooking
from django.contrib.auth.decorators import login_required
import json
from django.shortcuts import get_object_or_404
from datetime import date,timedelta,timezone,datetime
from django.contrib import messages
from django.http import JsonResponse


present=date.today()
def slot_list(request):
    now = date.today()
    max_slots_per_day = 10
    for shift in range(1,3):
        for i in range(5):
            current_date = now + timedelta(days=i)
            existing_slots = Slot.objects.filter(booking_date=current_date,shifts=shift)
            if existing_slots.count() < max_slots_per_day:
                slots_to_create = max_slots_per_day - existing_slots.count()
                for j in range(slots_to_create):
                    Slot.objects.create(
                        slot_number=j + 1,
                        is_selected=False,
                        is_available=True,
                        booking_date=current_date,
                        shifts=shift
                    )

    return render(request, 'Slot_booking.html')


def get_slots(request):
    if request.method == 'GET':
        selected_date = request.GET.get('selected_date')
        selected_shift=request.GET.get('selected_shift')
        slots = Slot.objects.filter(booking_date=selected_date,shifts=selected_shift)
        slot_data = [{'id': slot.id, 'slot_number': slot.slot_number, 'is_selected': slot.is_selected, 'is_available': slot.is_available} for slot in slots]

        return JsonResponse({'slots': slot_data})
    return JsonResponse({'slots': []})


def book_slot(request):
    if request.method == 'POST':
        slot_id = request.POST.get('slotid')
        slot = Slot.objects.get(id=slot_id)
        user = request.user

        # Check if the slot is available
        if not slot.is_available:
            return HttpResponse(json.dumps({"message": "Slot is already booked."}), content_type="application/json", status=400)
        
        booked_slots = Booking.objects.filter(user=user, slot__booking_date=slot.booking_date)
        if booked_slots.exists():
            return HttpResponse(json.dumps({"message": "You have already booked a slot for this date."}), content_type="application/json", status=400)

        else:


        # Create a booking record
            Booking.objects.create(user=user, slot=slot)

            HistoricalBooking.objects.create(user=user, slot=slot)

        # Mark the slot as selected
            slot.is_available = False
        
            slot.save()
        
            return HttpResponse(json.dumps({"message": "Slot booked successfully."}), content_type="application/json")
        
    return render(request,"Home.html")  

def user_bookings(request):
    
    user_bookings = Booking.objects.filter(user=request.user,slot__booking_date__gte=present)

    return render(request, 'My_bookings.html', {'user_bookings': user_bookings})

def cancel_slot(request, slot_id):
    slot = get_object_or_404(Slot, id=slot_id)
    booking = Booking.objects.filter(user=request.user, slot=slot).first()

    if booking:
        # Mark the slot as available
        slot.is_available = True
        slot.save()

        # Delete the booking record
        booking.delete()
        # Redirect to user's bookings
        return redirect('user_bookings')
    else:
        # Handle the case where the booking doesn't exist or doesn't belong to the user
        return HttpResponse("Booking not found or does not belong to you.")
    
def booking_history(request):
  
    historical_bookings = HistoricalBooking.objects.filter(user=request.user)
    return render(request, 'bookings_history.html', {'historical_bookings': historical_bookings})