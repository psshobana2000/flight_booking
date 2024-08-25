from django.contrib import admin
from .models import Place, Trip , AdminLogin, Airport, Passenger,Traveller,Profile



# Register your models here.
admin.site.register(Place)
admin.site.register(Trip)
admin.site.register(AdminLogin)
admin.site.register(Airport)
admin.site.register(Passenger)
admin.site.register(Traveller)
admin.site.register(Profile)


class AdminLoginAdmin(admin.ModelAdmin):
    list_display = ['username', 'email', 'ph_no', 'is_admin', 'is_staff', 'is_active', 'is_superuser']


