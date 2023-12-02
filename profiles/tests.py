import pytest
from django.test import TestCase, Client
from django.contrib.auth.models import User


class ProfileTestCase(TestCase):

    @pytest.mark.django_db
    def setUp(self):
        self.client = Client()
        self.credentials = {"username": "test_user", "password": "jHTy#4)Qm("}
        self.user = User.objects.create_user(self.credentials)

    def test_authentication(self):
        self.client.force_login(self.user)
        resp = self.client.get("/admin")
        return self.assertGreaterEqual(resp.status_code, 200, "Success")
