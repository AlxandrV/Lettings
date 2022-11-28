from django.urls import reverse
from django.test import TestCase

from lettings.models import Address, Letting


class TestLettings(TestCase):
    def test_lettings_index(self):
        path = reverse('lettings:index')
        res = self.client.get(path)

        # Assert
        self.assertTemplateUsed(res, 'lettings/index.html')
        self.assertEqual(res.status_code, 200)
        self.assertContains(res, text='<title>Lettings</title>', html=True)

    def test_lettings_letting(self):
        address_details = {
            'number': 10,
            'street': 'rue de la soif',
            'city': 'Paris',
            'state': 'IDF',
            'zip_code': '75000',
            'country_iso_code': 'FR'
        }
        address = Address.objects.create(**address_details)
        print(address.id)
        letting = Letting.objects.create(title='Bar de l\'U', address=address)
        path = reverse('lettings:letting', kwargs={'letting_id': letting.id })
        res = self.client.get(path)

        # Assert
        self.assertTemplateUsed(res, 'lettings/letting.html')
        self.assertEqual(res.status_code, 200)
        self.assertContains(res, text=f'<title>{letting.title}</title>', html=True)
