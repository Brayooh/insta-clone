from django.test import TestCase
from django.contrib.auth.models import User
from .models import *

class ProfileTest(TestCase):
    def setUp(self):
        self.user = User(username='user', email='email')
        self.user.save()
        self.profile = Profile(image='image', bio='bio', user=self.user)

    def test_instance(self):
        self.assertTrue(isinstance(self.profile, Profile))

    def test_save(self):
        self.profile.save_profile()
        profile = Profile.objects.all()
        self.assertTrue(len(profile)>0)


        self.assertTrue(len(comments)>0)
