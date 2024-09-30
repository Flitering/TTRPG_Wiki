from django.shortcuts import render, redirect, get_object_or_404
from .models import Character
from .forms import CharacterForm

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
