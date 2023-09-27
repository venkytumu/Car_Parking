from django.shortcuts import render, redirect, HttpResponse
from .models import Slot, Booking
from django.contrib.auth.decorators import login_required
import json
from datetime import date,timedelta
from django.contrib import messages
from django.http import JsonResponse

def slot_list(request):

    now = date.today()

    max_slots_per_day = 10

    for i in range(5):

        current_date = now + timedelta(days=i)

        existing_slots = Slot.objects.filter(booking_date=current_date)

        if existing_slots.count() < max_slots_per_day:

            # Calculate how many slots are needed to reach the maximum

            slots_to_create = max_slots_per_day - existing_slots.count()

            for j in range(slots_to_create):

                Slot.objects.create(

                    slot_number=j + 1,

                    is_selected=False,

                    is_available=True,

                    booking_date=current_date

                )
    return render(request, 'Slot_booking.html')

 

def get_slots(request):
    if request.method == 'GET':
        selected_date = request.GET.get('selected_date')
        slots = Slot.objects.filter(booking_date=selected_date)

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

        # Create a booking record
        Booking.objects.create(user=user, slot=slot)

        # Mark the slot as selected
        slot.is_available = False
        
        slot.save()
        
        return HttpResponse(json.dumps({"message": "Slot booked successfully."}), content_type="application/json")
        
    return HttpResponse(status=405)  # Method not allowed
