from django.test import TestCase
from mainApp.models import MyUUIDModel

class MyUUIDModelTest(TestCase):

    def test_uuid_is_created(self):
        thisID = MyUUIDModel.id
        self.assertEqual(type(thisID), 'String')


