from django.test import TestCase
from .models import Photo, Category, Location


# Create your tests here.
class CategoryTestClass(TestCase):
    def setUp(self):
        self.rare = Category(name="Sports")

    def test_save_category(self):
        self.rare.save_category()
        categories = Category.objects.all()
        self.assertTrue(len(categories) > 0)

    def test_delete_category(self):
        self.rare.save_category()
        categories = Category.objects.all()
        self.assertEqual(len(categories), 1)
        self.rare.delete_category()
        categories = Category.objects.all()
        self.assertEqual(len(categories), 0)

    def test_update_category(self):
        self.rare.save_category()
        self.rare.update_category(self.rare.id, 'Family')
        update = Category.objects.get(name="Family")
        self.assertTrue(update.name, 'Family')

    def test_display_categories(self):
        self.rare.save_category()
        self.assertEqual(len(Category.display_all_categories()), 1)


class LocationTestClass(TestCase):
    def setUp(self):
        self.office = Location(name='office')

    def test_location_instance(self):
        self.assertTrue(isinstance(self.office, Location))

    def test_save_location(self):
        self.office.save_location()
        places = Location.objects.all()
        self.assertTrue(len(places) > 0)

    def test_delete_location(self):
        self.office.save_location()
        places = Location.objects.all()
        self.assertEqual(len(places), 1)
        self.office.delete_location()
        places = Location.objects.all()
        self.assertEqual(len(places), 0)

    def test_display_locations(self):
        self.office.save_location()
        self.assertEqual(len(Location.display_all_locations()), 1)

    def test_update_location(self):
        self.office.save_location()
        self.office.update_location(self.office.id, 'office')
        update = Location.objects.get(location="office")
        self.assertTrue(update.name, 'Home')


class PhotoTestClass(TestCase):
    def setUp(self):
        self.Sports = Category(name='Sports')
        self.Paris = Location(location='Paris')
        self.liverpool = Photo(image='photo.jpeg', name='Klopp', description='Surprised', category=self.Sports,
                               location=self.Paris)

    def test_pic_instance(self):
        """
        test whether the new image created is an instance of the Image class
        """
        self.assertTrue(isinstance(self.liverpool, Photo))

    def test_save_pic(self):
        self.Sports.save_category()
        self.Paris.save_location()
        self.liverpool.save_photo()
        photo = Photo.objects.all()
        self.assertEqual(len(photo) > 0, 1)
