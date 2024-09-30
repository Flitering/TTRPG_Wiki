from django.shortcuts import render, redirect, get_object_or_404
from .models import Material
from .forms import MaterialForm

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
