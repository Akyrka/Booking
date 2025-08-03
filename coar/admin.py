from django.contrib import admin
from .models import Room, Customer, Booking

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('room', 'customer', 'start_time', 'end_time')
    list_filter = ('room', 'start_time')
    search_fields = ('customer__first_name', 'customer__last_name', 'room__number')

@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    list_display = ('number', 'peopl')

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name')
