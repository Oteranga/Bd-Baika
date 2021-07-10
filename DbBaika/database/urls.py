from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('people', views.all_people, name="people-data"),
    path('add_person', views.add_person, name="add-person"),
    path('list_people', views.list_people, name="list-people"),
    path('show_person/<person_id>', views.show_person, name="show-person"),
    path('update_person/<person_id>', views.update_person, name="update-person"),
    path('delete_person/<person_id>', views.delete_person, name="delete-person"),
]