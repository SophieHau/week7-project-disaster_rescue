from django.urls import path

from . import views

app_name = 'portal'
urlpatterns = [
	path('', views.index, name='index'),
	path('persons/show_safe', views.show_safe_persons, name='show_safe'),
	path('persons/show_missing', views.show_missing_persons, name='show_missing'),
	path('persons/show_all', views.show_all_persons, name='show_all'),
	path('persons/<int:person_id>', views.show_person, name='show_person'),
	path('persons/add', views.add_person, name='add_person'),
	path('persons/search_person', views.search_person, name='search_person'),
	path('persons/update/<int:person_id>', views.update_person, name='update_person'),
	path('persons/delete/<int:person_id>', views.delete_person, name='delete_person'),
	path('events/add', views.add_event, name='add_event'),
	path('events/show_all', views.show_events, name='show_events'),
	path('events/<int:event_id>', views.show_event, name='show_event'),
	path('events/update/<int:event_id>', views.update_event, name='update_event'),
	path('events/delete/<int:event_id>', views.delete_event, name='delete_event'),
	path('events/persons/<int:event_id>', views.show_persons_by_event, name='show_persons_by_event')
   # to do: add more paths...
]