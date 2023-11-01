from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from users.models import User
from vehicle.models import Moto, Milage


class MotoTestCase(APITestCase):

    def setUp(self):
        self.user = User.objects.create(email="test@test.ru", password='test', is_staff=True, is_superuser=True)
        self.client.force_authenticate(user=self.user)

        self.moto = Moto.objects.create(name="Harley-Davidson Ultra Limited", description='test')
        self.milage = Milage.objects.create(moto=self.moto, distance=1000, year="2021")
        self.data = {
            "name": "Honda CBF 1000",
            "description": "test",
            "milage": [
                {
                    "distance": 2000,
                    "year": "2020"
                }
            ]
        }

    def test_detail(self):
        response = self.client.get(
            reverse('vehicle:moto-detail', args=[self.moto.pk])
        )

        self.assertEquals(
            response.status_code,
            status.HTTP_200_OK
        )

        self.assertEquals(
            response.json(),
            {
                "id": self.moto.pk,
                "name": self.moto.name,
                "description": self.moto.description,
                "owner": self.moto.owner,
                "last_milage": 1000,
                'price': None,
                'usd_price': None
            }
        )
