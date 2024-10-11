from django.shortcuts import render, redirect, get_object_or_404
from .models import Material
from .forms import MaterialForm
from django.contrib import messages

def material_list(request):
    materials = Material.objects.all()
    return render(request, 'materials/material_list.html', {'materials': materials})

def material_detail(request, id):
    material = get_object_or_404(Material, id=id)
    return render(request, 'materials/material_detail.html', {'material': material})

def add_material(request):
    if request.method == 'POST':
        form = MaterialForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('material_list')
    else:
        form = MaterialForm()
    return render(request, 'materials/add_material.html', {'form': form})

def material_list(request):
    query = request.GET.get('q')
    if query:
        materials = Material.objects.filter(title__icontains=query)
    else:
        materials = Material.objects.all()
    return render(request, 'materials/material_list.html', {'materials': materials})

def edit_material(request, id):
    material = get_object_or_404(Material, id=id)
    if request.method == 'POST':
        form = MaterialForm(request.POST, instance=material)
        if form.is_valid():
            form.save()
            return redirect('material_detail', id=material.id)
    else:
        form = MaterialForm(instance=material)
    return render(request, 'materials/edit_material.html', {'form': form, 'material': material})

def delete_material(request, id):
    material = get_object_or_404(Material, id=id)
    if request.method == 'POST':
        material.delete()
        messages.success(request, 'Материал успешно удалён.')
        return redirect('material_list')
    return render(request, 'materials/delete_material.html', {'material': material})