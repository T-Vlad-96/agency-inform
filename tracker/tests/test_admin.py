from django.test import TestCase, Client
from django.contrib.auth import get_user_model
from django.urls import reverse


class RedactorAdminTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.admin_user = get_user_model().objects.create_superuser(
            username="admin",
            password="Abc12345",
        )
        self.client.force_login(self.admin_user)
        self.user_redactor = get_user_model().objects.create_user(
            username="user_redactor",
            password="Abc12345",
            years_of_experience=2,
        )

    def test_redactor_experience_listed(self):
        url = reverse("admin:tracker_redactor_changelist")
        response = self.client.get(url)
        self.assertContains(response, self.user_redactor.years_of_experience)

