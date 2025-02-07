from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse


TOPIC_LIST_URL = reverse("tracker:topic_list")
TOPIC_CREATE_URL = reverse("tracker:topic_create")
TOPIC_UPDATE_URL = reverse("tracker:topic_update", kwargs={"pk": 1})
TOPIC_DELETE_URL = reverse("tracker:topic_delete", kwargs={"pk": 1})


class PublicTopicTests(TestCase):

    def test_topic_list_login_required(self):
        response = self.client.get(TOPIC_LIST_URL)
        self.assertNotEquals(response.status_code, 200)

    def test_topic_create_login_required(self):
        response = self.client.get(TOPIC_CREATE_URL)
        self.assertNotEquals(response.status_code, 200)

    def test_topic_update_login_required(self):
        response = self.client.get(TOPIC_UPDATE_URL)
        self.assertNotEquals(response.status_code, 200)

    def test_topic_delete_login_required(self):
        response = self.client.get(TOPIC_DELETE_URL)
        self.assertNotEquals(response.status_code, 200)