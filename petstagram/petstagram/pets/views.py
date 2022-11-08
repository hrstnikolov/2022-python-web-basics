from django.shortcuts import render

from petstagram.pets.models import Pet


def add_pet(request):
    return render(request, 'pets/pet-add-page.html')


def delete_pet(request, username, pet_slug):
    return render(request, 'pets/pet-delete-page.html')


def display_pet(request, username, pet_slug):
    pet = Pet.objects.get(slug=pet_slug)
    # TODO: fix when auth
    # user = User..
    context = {
        'pet': pet,
        'photos': pet.photo_set.all()
    }
    return render(request, 'pets/pet-details-page.html', context)


def edit_pet(request, username, pet_slug):
    return render(request, 'pets/pet-edit-page.html')
