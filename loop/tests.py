from django.test import TestCase

from .models import *

class NeighborhoodTest(TestCase):

    def setUp(self):

        self.user = User.objects.create(id = 1, username='bmn')
        self.profile = profileUser.objects.create(user=self.user, bio='always on top', location='home', business='news', profile_name='Yes sir', email='weo@dod.com', )

    def tes_instance(self):
        self.assertTrue(isinstance(self.profile, profileUser))
    
    def get_profile(self):
        self.profile.save()
        profile = profileUser.get_profile()
        self.assertTrue(len(profile) > 0)


class PostTest(TestCase):
    def instance(self):
        self.posts = Posts.objects.create(owner='bmn', title='you won', content='alright man')

        self.assertTrue(isinstance(self.posts, Posts))

    def tearDown(self):
         self.posts = Posts.objects.create(owner='bmn', title='you won', content='alright man')
         self.posts.save()
         print(self.posts)
         self.posts.delete()        