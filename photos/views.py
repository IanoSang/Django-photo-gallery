from django.shortcuts import render
from .models import Category, Photo

# Create your views here.

def gallery(request):
    categories = Category.objects.all()
    context = {'categories': categories}
    return render(request, 'photos/gallery.html', context)


def view_photo(request, pk):
    return render(request, 'photos/photo.html')


def add_photo(request):
    return render(request, 'photos/add.html')
