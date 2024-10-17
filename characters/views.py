from django.shortcuts import render, redirect, get_object_or_404
from .models import Character
from .forms import CharacterForm

def create_character(request):
    if request.method == 'POST':
        form = CharacterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('character_list')
    else:
        form = CharacterForm()
    return render(request, 'characters/create_character.html', {'form': form})


def character_list(request):
    characters = Character.objects.all()
    return render(request, 'characters/character_list.html', {'characters': characters})

def character_detail(request, id):
    character = get_object_or_404(Character, id=id)
    return render(request, 'characters/character_detail.html', {'character': character})

def create_character(request):
    if request.method == 'POST':
        form = CharacterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('character_list')
    else:
        form = CharacterForm()
    return render(request, 'characters/create_character.html', {'form': form})

def edit_character(request, id):
    character = get_object_or_404(Character, id=id)
    if request.method == 'POST':
        form = CharacterForm(request.POST, instance=character)
        if form.is_valid():
            form.save()
            return redirect('character_detail', id=character.id)
    else:
        form = CharacterForm(instance=character)
    return render(request, 'characters/edit_character.html', {'form': form, 'character': character})

def delete_character(request, id):
    character = get_object_or_404(Character, id=id)
    if request.method == 'POST':
        character.delete()
        return redirect('character_list')
    return render(request, 'characters/delete_character.html', {'character': character})

def character_list(request):
    query = request.GET.get('q')
    if query:
        characters = Character.objects.filter(name__icontains=query)
    else:
        characters = Character.objects.all()
    return render(request, 'characters/character_list.html', {'characters': characters})

