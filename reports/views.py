from django.shortcuts import render, redirect
from .models import LostItem, FoundItem
from django import forms

class LostItemForm(forms.ModelForm):
    class Meta:
        model = LostItem
        fields = '__all__'

class FoundItemForm(forms.ModelForm):
    class Meta:
        model = FoundItem
        fields = '__all__'

def home(request):
    lost_items = LostItem.objects.all().order_by('-id')
    found_items = FoundItem.objects.all().order_by('-id')
    return render(request, 'home.html', {'lost_items': lost_items, 'found_items': found_items})

def report_lost(request):
    if request.method == 'POST':
        form = LostItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = LostItemForm()
    return render(request, 'form.html', {'form': form, 'title': 'Report Lost Item'})

def report_found(request):
    if request.method == 'POST':
        form = FoundItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = FoundItemForm()
    return render(request, 'form.html', {'form': form, 'title': 'Report Found Item'})
