from django.urls import reverse
from django.test import TestCase

from lettings.models import Address, Letting


class TestLettings(TestCase):
    def test_oc_lettings_site_index(self):
        path = reverse('index')
        res = self.client.get(path)

        # Assert
        self.assertTemplateUsed(res, 'index.html')
        self.assertEqual(res.status_code, 200)
        self.assertContains(res, text='<title>Holiday Homes</title>', html=True)
