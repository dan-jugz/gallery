from django.test import TestCase
from .models import User,Image,tags
import datetime as dt

# Create your tests here.
class UserTestClass(TestCase):
# Set up method
    def setUp(self):
        self.daniel= User(first_name = 'Daniel', last_name ='Njuguna', email ='njuguna@moringaschool.com')
    
    # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.daniel,User))

    def test_save_method(self):
        self.daniel.save_user()
        users = User.objects.all()
        self.assertTrue(len(users) > 0)