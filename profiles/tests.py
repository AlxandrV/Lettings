from django.urls import reverse
from django.test import TestCase
from django.contrib.auth.models import User

from profiles.models import Profile


class TestLettings(TestCase):
    def test_profiles_index(self):
        path = reverse('profiles:index')
        res = self.client.get(path)

        # Assert
        self.assertTemplateUsed(res, 'profiles/index.html')
        self.assertEqual(res.status_code, 200)
        self.assertContains(res, text='<title>Profiles</title>', html=True)

    def test_profiles_profile(self):
        user = User.objects.create(username='test user')
        profile = Profile.objects.create(user=user, favorite_city='test City')
        path = reverse('profiles:profile', kwargs={'username': user.username })
        res = self.client.get(path)

        # Assert
        self.assertTemplateUsed(res, 'profiles/profile.html')
        self.assertEqual(res.status_code, 200)
        self.assertContains(res, text=f'<title>{profile.user.username}</title>', html=True)
