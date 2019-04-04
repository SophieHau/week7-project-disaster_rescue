from django.shortcuts import get_object_or_404, redirect, render
from django.db.models import Q

from .models import PersonStatus, Person
from .forms import PersonForm

def index(request):
    return render(request, 'portal/index.html')


def add_person(request):
    if request.method == 'POST':
        person = PersonForm(request.POST)
        person.save()
        return redirect('portal:index')
    form = PersonForm()
    return render(request, 'portal/add_person.html', {
            'form': form
        })


def show_person(request, person_id):
    # ... 
    person = Person.objects.get(id=person_id)
    return render(request, 'portal/show_person.html', {
            'person': person })


def show_safe_persons(request):
    persons = Person.objects.filter(status__name='safe')
    return render(request, 'portal/show_persons.html', {
        'title': 'Persons marked as Safe',
        'main_heading': 'Persons Marked as Safe',
        'persons': persons })


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
        # form = PersonForm(request.POST, initial={
        #     'first_name': person.first_name,
        #     'last_name': person.last_name,
        #     'other_name': person.other_name,
        #     'status': person.status,
        #     'id_number': person.id_number,
        #     'dob': person.dob,
        #     'mobile': person.mobile,
        #     'email': person.email,
        #     'description': person.description,
        #     })
        person_form = PersonForm(request.POST, instance=person)

        if person_form.is_valid():
            person_form.save()
            return redirect('portal:index')
        else:
            print('error')

    person_form = PersonForm(instance=person)
    return render(request, 'portal/update.html', {
        'form': person_form,
        'person': person
        })