from django.shortcuts import render, redirect
from .models import Category, Photo


# Create your views here.

def gallery(request):
    category = request.GET.get('category')
    photos = Photo.objects.all()
    categories = Category.objects.all()
    context = {'categories': categories, 'photos': photos}
    return render(request, 'photos/gallery.html', context)


def view_photo(request, pk):
    photo = Photo.objects.get(id=pk)
    categories = Category.objects.all()
    context = {'categories': categories, 'photo': photo}
    return render(request, 'photos/photo.html', context)


def add_photo(request):
    categories = Category.objects.all()
    context = {'categories': categories}

    if request.method == 'POST':
        data = request.POST
        images = request.FILES.getlist('images')

        if data['category'] != 'none':
            category = Category.objects.get(id=data['category'])
        elif data['category_new'] != '':
            category, created = Category.objects.get_or_create(
                name=data['category_new'])
        else:
            category = None

        for image in images:
            photo = Photo.objects.create(
                category=category,
                description=data['description'],
                image=image,
            )

        return redirect('gallery')

    return render(request, 'photos/add.html', context)
