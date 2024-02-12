from django.contrib import admin
from .models import Address, Profile
# Register your models here.


class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'isVip', 'phoneNumber',]
    list_filter = ['isVip',]


class AddressAdmin(admin.ModelAdmin):
    list_display = ['user', 'country', 'postalCode',]
    list_filter = ['postalCode', 'city', 'user']


admin.site.register(Profile, ProfileAdmin)
admin.site.register(Address, AddressAdmin)
