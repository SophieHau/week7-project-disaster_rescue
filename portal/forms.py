from django.db import models
from django.forms import ModelForm
from .models import Person, Event




class PersonForm(ModelForm):
    class Meta:
        model = Person
        fields = ['first_name', 'last_name', 'other_name', 'status', 'id_number', 'dob', 'mobile', 'email', 'description', 'event']


class EventForm(ModelForm):
	class Meta:
		model = Event
		fields = ['name', 'end_date', 'location', 'severity', 'category', 'image']
