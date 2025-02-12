from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse

from tracker.models import Redactor


REDACTOR_LIST_URL = reverse("tracker:redactor_list")
REDACTOR_CREATE_URL = reverse("tracker:redactor_create")
REDACTOR_DETAIL_URL = reverse(
    "tracker:redactor_detail", kwargs={"pk": 1}
)
REDACTOR_UPDATE_URL = reverse(
    "tracker:redactor_update",kwargs={"pk": 1}
)
REDACTOR_DELETE_URL = reverse(
    "tracker:redactor_delete", kwargs={"pk": 1}
)


class RedactorViewPublicTests(TestCase):

    def test_redactor_list_public(self):
        response = self.client.get(REDACTOR_LIST_URL)
        self.assertNotEquals(response.status_code, 200)
        self.assertRedirects(
            response,
            f"{reverse('login')}?next={REDACTOR_LIST_URL}",
        )

    def test_redactor_create_public(self):
        response = self.client.get(REDACTOR_CREATE_URL)
        self.assertNotEquals(response.status_code, 200)
        self.assertRedirects(
            response,
            f"{reverse('login')}?next={REDACTOR_CREATE_URL}"
        )

    def test_redactor_detail_public(self):
        response = self.client.get(REDACTOR_DETAIL_URL)
        self.assertNotEquals(response.status_code, 200)
        self.assertRedirects(
            response,
            f"{reverse('login')}?next={REDACTOR_DETAIL_URL}"
        )

    def test_redactor_update_public(self):
        response = self.client.get(REDACTOR_UPDATE_URL)
        self.assertNotEquals(response.status_code, 200)
        self.assertRedirects(
            response,
            f"{reverse('login')}?next={REDACTOR_UPDATE_URL}"
        )

    def test_redactor_delete_public(self):
        response = self.client.get(REDACTOR_DELETE_URL)
        self.assertNotEquals(response.status_code, 200)
        self.assertRedirects(
            response,
            f"{reverse('login')}?next={REDACTOR_DELETE_URL}"
        )


class RedactorListViewPrivateTests(TestCase):

    def setUp(self):
        user = User.objects.create_user(
            username="test",
            password="password"
        )
        self.client.force_login(user)
