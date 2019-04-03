#!/usr/bin/env python3

import os
import random

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'dr.settings')

import django
django.setup()

from faker import Faker

from portal.models import Event, PersonStatus, Person


Event.objects.all().delete()
PersonStatus.objects.all().delete()

fire_event = Event(name='fire_sale')
fire_event.save()

missing_status = PersonStatus(name='missing')
missing_status.save()

safe_status = PersonStatus(name='safe')
safe_status.save()

# to do: create 30 Person objects using Faker
fake = Faker()

def fake_first_name():
	return fake.first_name()

def fake_last_name():
	return fake.last_name()

def fake_other_name():
	return fake.name()

def fake_id_number():
	return random.randint(1000, 100000)

def fake_dob():
	return fake.date()

def fake_mobile():
	return fake.phone_number()

def fake_email():
	return fake.email()

def fake_description():
	return fake.sentence()

def generate_status():
	statuses = PersonStatus.objects.all()
	status = random.choice(statuses)
	return status

def generate_person(number):
	for i in range (0, number):
		p = Person(
			first_name=fake_first_name(),
			last_name=fake_last_name(),
			status=generate_status(),
			id_number=fake_id_number(),
			dob=fake_dob(),
			mobile=fake_mobile(),
			email=fake_email(),
			description=fake_description(),
			)

		p.save()

# generate_person(30)




