from django.shortcuts import render, redirect
from .models import Category, Photo, Location


# Create your views here.

def gallery(request):
    location = request.GET.get('location')
    if location == None:
        photos = Photo.objects.filter()
    else:
        photos = Photo.objects.filter(
            location__name=location)
    locations = Location.objects.all()
    categories = Category.objects.all()
    context = {'categories': categories, 'photos': photos, 'locations':locations}
    return render(request, 'photos/gallery.html', context)


def view_photo(request, pk):
    photo = Photo.objects.get(id=pk)
    locations = Location.objects.all()
    categories = Category.objects.all()
    context = {'categories': categories, 'photo': photo, 'locations':locations}
    return render(request, 'photos/photo.html', context)


def add_photo(request):
    categories = Category.objects.all()
    locations = Location.objects.all()
    context = {'categories': categories, 'locations':locations}

    if request.method == 'POST':
        data = request.POST
        images = request.FILES.getlist('images')

        if data['category'] != 'none':
            category = Category.objects.get(id=data['category'])
        elif data['category_new'] != '':
            category, created = Category.objects.get_or_create(
                name=data['category_new'])
        else:
            category =None
        if data['location'] != 'none':
            location = Location.objects.get(id=data['location'])
        elif data['location_new'] != '':
            location, created = Location.objects.get_or_create(
                name=data['location_new'])
        else:
            location = None

        for image in images:
            photo = Photo.objects.create(
                location=location,
                category=category,
                description=data['description'],
                name=data['name'],
                image=image,
            )

        return redirect('gallery')

    return render(request, 'photos/add.html', context)


def search_results(request):

    if 'photos' in request.GET and request.GET["photos"]:
        locations = Location.objects.all()
        search_term = request.GET.get("photos")
        searched_photos = Photo.search_by_category(search_term)
        message = f"{search_term}"
        print(searched_photos)
        return render(request, 'photos/search.html',{"message":message,"photos": searched_photos, 'locations':locations})
    else:
        message = "You haven't searched for any category"
        return render(request, 'photos/search.html',{"message":message})
