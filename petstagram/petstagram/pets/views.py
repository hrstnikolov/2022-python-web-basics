from django.shortcuts import render, redirect

from petstagram.pets.forms import PetCreateForm, PetEditForm
from petstagram.pets.models import Pet


def add_pet(request):
    if request.method == 'GET':
        form = PetCreateForm()
    else:
        form = PetCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('display user', pk=1)  # TODO: fix when auth
    context = {
        'form': form,
    }

    return render(
        request,
        'pets/pet-add-page.html',
        context,
    )


def edit_pet(request, username, pet_slug):
    edited_pet = Pet.objects.filter(slug=pet_slug)  # TODO: fix when auth
    if request.method == 'GET':
        form = PetEditForm(data=request.POST)
    else:
        form = PetEditForm(
            data=request.POST,
            instance=edited_pet,
        )
        if form.is_valid():
            form.save()
            return redirect('display user', pk=1)  # TODO: fix when auth
    context = {
        'form': form,
        'pet': edited_pet,
    }

    return render(
        request,
        'pets/pet-edit-page.html',
        context,
    )


def display_pet(request, username, pet_slug):
    pet = Pet.objects.get(slug=pet_slug)
    # TODO: fix when auth
    # user = User..
    context = {
        'pet': pet,
        'photos': pet.photo_set.all()
    }
    return render(request, 'pets/pet-details-page.html', context)


def delete_pet(request, username, pet_slug):
    return render(request, 'pets/pet-delete-page.html')
