from django.contrib import admin
from .models import Event, PersonStatus, Person


# to do: register models for Admin app to use

admin.site.register(Event)
admin.site.register(PersonStatus)
admin.site.register(Person)
