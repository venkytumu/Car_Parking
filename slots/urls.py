# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path("slot_list", views.slot_list, name='slot-list'),

    path("get_slots", views.get_slots, name='get_slots'),

    # path("book_slot", views.book_slot, name='book_slot'),

    path("book_slot", views.book_slot, name='book_slot'),
   
    # path("logout",views.logout,name="logout")
]
