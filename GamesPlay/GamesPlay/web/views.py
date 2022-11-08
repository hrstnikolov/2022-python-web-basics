from django.core.exceptions import ValidationError
from django.db.models import Avg
from django.shortcuts import render, redirect

from GamesPlay.web.forms import ProfileCreateForm, GameCreateForm, GameEditForm, GameDeleteForm, ProfileEditForm, \
    ProfileDeleteForm
from GamesPlay.web.models import Profile, Game


def get_profile():
    try:
        return Profile.objects.get()
    except Profile.DoesNotExist:
        return None


def index(request):
    profile = get_profile()
    hide_nav = True if not profile else False

    context = {
        'hide_nav': hide_nav,
    }
    return render(request, 'core/home-page.html', context)


def dashboard(request):
    games = Game.objects.all()

    context = {
        'games': games,
    }

    return render(request, 'core/dashboard.html', context)


def create_game(request):
    if request.method == 'GET':
        form = GameCreateForm()
    else:
        form = GameCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    context = {
        'form': form,
    }
    return render(request, 'game/create-game.html', context)


def details_game(request, pk):
    game = Game.objects.filter(pk=pk).get()
    context = {
        'game': game,
    }
    return render(request, 'game/details-game.html', context)


def edit_game(request, pk):
    game = Game.objects.filter(pk=pk).get()

    if request.method == 'GET':
        form = GameEditForm(instance=game)
    else:
        form = GameEditForm(request.POST, instance=game)
        if form.is_valid():
            form.save()
            return redirect('dashboard')

    context = {
        'form': form,
        'game': game,
    }

    return render(request, 'game/edit-game.html', context)


def delete_game(request, pk):
    game = Game.objects.filter(pk=pk).get()

    if request.method == 'GET':
        form = GameDeleteForm(instance=game)
    else:
        form = GameDeleteForm(request.POST, instance=game)
        if form.is_valid():
            form.save()
            return redirect('dashboard')

    context = {
        'form': form,
        'game': game,
    }
    return render(request, 'game/delete-game.html', context)


def create_profile(request):
    hide_nav = True

    if request.method == 'GET':
        form = ProfileCreateForm()
    else:
        form = ProfileCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')

    context = {
        'form': form,
        'hide_nav': hide_nav,
    }

    return render(request, 'profile/create-profile.html', context)


def edit_profile(request):
    profile = get_profile()
    if request.method == 'GET':
        form = ProfileEditForm(instance=profile)
    else:
        form = ProfileEditForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('details profile')
    context = {
        'form': form,
    }
    return render(request, 'profile/edit-profile.html', context)


def details_profile(request):
    profile = get_profile()
    games_count = Game.objects.count()
    if games_count == 0:
        average_rating = 0
    else:
        average_rating = Game.objects.aggregate(Avg('rating'))['rating__avg']

    context = {
        'profile': profile,
        'games_count': games_count,
        'average_rating': average_rating,
    }
    return render(request, 'profile/details-profile.html', context)


def delete_profile(request):
    profile = get_profile()

    if request.method == 'GET':
        form = ProfileDeleteForm(instance=profile)
    else:
        form = ProfileDeleteForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('index')

    context = {
        'form': form,
    }
    return render(request, 'profile/delete-profile.html', context)
