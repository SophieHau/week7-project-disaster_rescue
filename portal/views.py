from django.shortcuts import get_object_or_404, redirect, render
from django.db.models import Q
from django.contrib import messages
from .models import PersonStatus, Person, Event
from .forms import PersonForm, EventForm

def index(request):
    return render(request, 'portal/index.html')


def add_person(request):
    if request.method == 'POST':
        person = PersonForm(request.POST)
        person.save()
        messages.success(request, 'Profile added.')
        return redirect('portal:show_all')
    form = PersonForm()
    return render(request, 'portal/add_person.html', {
            'form': form
        })


def show_person(request, person_id):
    # ... 
    person = Person.objects.get(id=person_id)
    return render(request, 'portal/show_person.html', {
            'person': person })

def delete_person(request, person_id):
    if request.method == 'POST':
        person = Person.objects.get(id=person_id)
        person.delete()
        messages.info(request, 'Profile deleted.')
    return redirect('portal:show_all')


def show_safe_persons(request):
    persons = Person.objects.filter(status__name='safe')
    return render(request, 'portal/show_persons.html', {
        'title': 'Persons marked as Safe',
        'main_heading': 'Persons Marked as Safe',
        'persons': persons })

def show_missing_persons(request):
    persons = Person.objects.filter(status__name='missing')
    return render(request, 'portal/show_persons.html', {
            'title': 'Persons marked as missing',
            'main_heading': 'Persons Marked as Missing',
            'persons': persons
        })

def show_all_persons(request):
    persons = Person.objects.all()
    return render(request, 'portal/show_persons.html', {
            'title': 'All persons registered',
            'main_heading': 'All Persons Registered',
            'persons': persons,
        })

def search_person(request):
    context = None
    if request.method != 'POST':
        return redirect('portal:index')

    text = request.POST.get('search', '')
    results = Person.objects.filter(
        Q(first_name__icontains=text) |
        Q(last_name__icontains=text) |
        Q(other_name__icontains=text) |
        Q(description__icontains=text))

    return render(request, 'portal/search_results.html', {
            'results': results
        })

def update_person(request, person_id):
    person = Person.objects.get(id=person_id)

    if request.method == 'POST':
        person_form = PersonForm(request.POST, instance=person)

        if person_form.is_valid():
            person_form.save()
            messages.success(request, 'Profile details updated.')
            return redirect('portal:show_person', person_id=person_id)

    person_form = PersonForm(instance=person)
    return render(request, 'portal/update.html', {
        'form': person_form,
        'person': person
        })

def add_event(request):
    if request.method == 'POST':
        event = EventForm(request.POST)
        event.save()
        messages.success(request, 'Event added.')
        return redirect('portal:show_events')
    form = EventForm()
    return render(request, 'portal/add_event.html', {
            'form': form
        })


def show_events(request):
    events = Event.objects.order_by('-start_date')
    return render(request, 'portal/show_events.html', {
            'title': 'Events',
            'main_heading': 'Events List',
            'events': events
        })

def show_event(request, event_id):
    event = Event.objects.get(id=event_id)
    return render(request, 'portal/show_event.html', {
            'event': event
        })


def update_event(request, event_id):
    event = Event.objects.get(id=event_id)
    if request.method == 'POST':
        event_form = EventForm(request.POST, instance=event)

        if event_form.is_valid():
            event_form.save()
            messages.success(request, 'Event details updated.')
            return redirect('portal:show_event', event_id=event_id)

    event_form = EventForm(instance=event)
    return render(request, 'portal/update_event.html', {
        'form': event_form,
        'event': event
        })

def delete_event(request, event_id):
    if request.method == 'POST':
        event = Event.objects.get(id=event_id)
        event.delete()
        messages.info(request, 'Event deleted.')
    return redirect('portal:show_events')


