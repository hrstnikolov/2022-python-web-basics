from django.urls import path, include

from petstagram.pets.views import add_pet, delete_pet, display_pet, edit_pet

urlpatterns = (
    path('add/', add_pet, name='add pet'),
    path('<str:username>/pet/<slug:pet_name>/', include([
        path('', display_pet, name='display pet'),
        path('edit/', edit_pet, name='edit pet'),
        path('delete/', delete_pet, name='delete pet'),
    ])),
)
