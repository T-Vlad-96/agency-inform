from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse

NEWSPAPER_LIST = reverse("tracker:newspaper_list")
NEWSPAPER_CREATE = reverse("tracker:newspaper_create")
NEWSPAPER_DETAIL = reverse(
    "tracker:newspaper_detail",
    kwargs={"pk": 1}
)
NEWSPAPER_UPDATE = reverse(
    "tracker:newspaper_update",
    kwargs={"pk": 1}
)
NEWSPAPER_DELETE = reverse(
    "tracker:newspaper_delete",
    kwargs={"pk": 1}
)


class NewspaperViewsPublicTests(TestCase):

    def test_newspaper_list_public(self):
        response = self.client.get(NEWSPAPER_LIST)
        self.assertNotEqual(
            response.status_code,
            200
        )

    def test_newspaper_create_public(self):
        response = self.client.get(NEWSPAPER_CREATE)
        self.assertNotEqual(
            response.status_code,
            200
        )

    def test_newspaper_detail_public(self):
        response = self.client.get(NEWSPAPER_DETAIL)
        self.assertNotEqual(
            response.status_code,
            200
        )

    def test_newspaper_update_public(self):
        response = self.client.get(NEWSPAPER_UPDATE)
        self.assertNotEqual(
            response.status_code,
            200
        )

    def test_newspaper_delete_public(self):
        response = self.client.get(NEWSPAPER_DELETE)
        self.assertNotEqual(
            response.status_code,
            200
        )
