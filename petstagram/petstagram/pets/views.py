from django.shortcuts import render


def add_pet(request):
    return render(request, 'pets/pet-add-page.html')


def delete_pet(request, username, pet_slug):
    return render(request, 'pets/pet-delete-page.html')


def display_pet(request, username, pet_slug):
    return render(request, 'pets/pet-details-page.html')


def edit_pet(request, username, pet_slug):
    return render(request, 'pets/pet-edit-page.html')
