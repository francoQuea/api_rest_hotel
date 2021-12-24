from django.contrib import admin
from hotel_api.models import State, Room, Client, Invoice, Payment, Reservation

admin.site.register(State)
admin.site.register(Room)
admin.site.register(Client)
admin.site.register(Invoice)
admin.site.register(Payment)
admin.site.register(Reservation)
