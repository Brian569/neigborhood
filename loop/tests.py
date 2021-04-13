from django.test import TestCase

from .models import *

class ProfileTest(TestCase):

    def setUp(self):

        self.user = User.objects.create(id = 1, username='bmn')
        self.profile = profileUser.objects.create(user=self.user, bio='always on top', location='home', business='news', profile_name='Yes sir', email='weo@dod.com', )

    def tes_instance(self):
        self.assertTrue(isinstance(self.profile, profileUser))
    
    def get_profile(self):
        self.profile.save()
        profile = profileUser.save_user()
        self.assertTrue(len(profile) > 0)
    
class PostTest(TestCase):

    def setUp(self):
         self.posts = Posts.objects.create(owner='bmn', title='you won', content='alright man')

    def save_post(self):
        self.posts.save()

    def instance(self):      
        self.assertTrue(isinstance(self.posts, Posts))

    def tearDown(self):
         self.posts = Posts.objects.create(owner='bmn', title='you won', content='alright man')
 
         self.posts.delete()        