from django.contrib import admin
from deliveryapp.models import Contact, Member, Order, Feedback, Driver
#Register your models here.
admin.site.register(Contact)
admin.site.register(Member)

admin.site.register(Order)
admin.site.register(Feedback)
admin.site.register(Driver)
