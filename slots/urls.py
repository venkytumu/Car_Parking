# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path("slot_list", views.slot_list, name='slot-list'),

    path("get_slots", views.get_slots, name='get_slots'),

    # path("book_slot", views.book_slot, name='book_slot'),

    path("book_slot", views.book_slot, name='book_slot'),

    path("user_bookings", views.user_bookings, name='user_bookings'),
    
    path("cancel_slot/<int:slot_id>/", views.cancel_slot, name='cancel_slot'),

    path("booking_history", views.booking_history, name='booking_history'),
    # path("logout",views.logout,name="logout")
     path("list_notifications", views.list_notifications, name='list_notifications'),

    path("mark_notification_as_read/<int:notification_id>/", views.mark_notification_as_read, name='mark_notification_as_read'),
]
