from django.db import models


# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=60, null=False, blank=False)

    def __str__(self):
        return self.name

    def save_category(self):
        self.save()

    def delete_category(self):
        self.delete()

    @classmethod
    def update_category(cls, id, name):
        cls.objects.filter(id=id).update(name=name)

    @classmethod
    def display_all_categories(cls):
        return cls.objects.all()


class Location(models.Model):
    name = models.CharField(max_length=60, null=False, blank=False)

    def __str__(self):
        return self.name

    def save_location(self):
        self.save()

    def delete_location(self):
        self.delete()

    @classmethod
    def update_location(cls, id, name):
        cls.objects.filter(id=id).update(loc=name)

    @classmethod
    def display_all_locations(cls):
        return cls.objects.all()


class Photo(models.Model):
    name = models.CharField(max_length=60, null=False, blank=True)
    category = models.ForeignKey(Category, null=True, on_delete=models.SET_NULL)
    location = models.ForeignKey(Location, null=True, blank=True, on_delete=models.SET_NULL)
    image = models.ImageField(null=False, blank=False)
    description = models.TextField()

    def __str__(self):
        return self.description

    class Meta:
        ordering = ['-id']

    @classmethod
    def get_all_photos(cls):
        photos = Photo.objects.all()
        return photos

    @classmethod
    def get_photo_by_id(cls, id):
        photo = cls.objects.get(id=id)
        return photo

    @classmethod
    def search_by_category(cls, search_term):
        category = cls.objects.filter(category__name__icontains=search_term)
        return category

    @classmethod
    def filter_by_location(cls, location):
        photos = Photo.objects.filter(location__name=location)
        return photos

    @classmethod
    def display_all_images(cls):
        return cls.objects.all()

    def save_photo(self):
        self.save()

    def update_photo(self, name, description, category):
        self.name = name,
        self.description = description,
        self.category = category
        self.save()



