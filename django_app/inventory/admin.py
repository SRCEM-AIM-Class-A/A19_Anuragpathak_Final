from django.contrib import admin
from .models import Vehicle

@admin.register(Vehicle)
class VehicleAdmin(admin.ModelAdmin):
    list_display = ('name', 'vehicle_type')  # Show these columns in admin list view
    search_fields = ('name', 'vehicle_type')  # Add search bar
