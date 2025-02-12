from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse

from tracker.models import Topic

TOPIC_LIST_URL = reverse("tracker:topic_list")
TOPIC_CREATE_URL = reverse("tracker:topic_create")
TOPIC_UPDATE_URL = reverse("tracker:topic_update", kwargs={"pk": 1})
TOPIC_DELETE_URL = reverse("tracker:topic_delete", kwargs={"pk": 1})


class PublicTopicViewsTests(TestCase):
    def setUp(self):
        Topic.objects.create(name="test")

    def test_topic_list_login_required(self):
        response = self.client.get(TOPIC_LIST_URL)
        self.assertNotEquals(response.status_code, 200)
        self.assertRedirects(
            response,
            f"{reverse('login')}?next={TOPIC_LIST_URL}"
        )

    def test_topic_create_login_required(self):
        response = self.client.get(TOPIC_CREATE_URL)
        self.assertNotEquals(response.status_code, 200)
        self.assertRedirects(
            response,
            f"{reverse('login')}?next={TOPIC_CREATE_URL}"
        )

    def test_topic_update_login_required(self):
        response = self.client.get(TOPIC_UPDATE_URL)
        self.assertNotEquals(response.status_code, 200)
        self.assertRedirects(
            response,
            f"{reverse('login')}?next={TOPIC_UPDATE_URL}"
        )

    def test_topic_delete_login_required(self):
        response = self.client.get(TOPIC_DELETE_URL)
        self.assertNotEquals(response.status_code, 200)
        self.assertRedirects(
            response,
            f"{reverse('login')}?next={TOPIC_DELETE_URL}"
        )


class PrivateTopicListViewTests(TestCase):
    def setUp(self):
        user = get_user_model().objects.create_user(
            username="test_user",
            password="test_password",
        )
        self.client.force_login(user)
        number_of_topics = 7
        for i in range(number_of_topics):
            Topic.objects.create(
                name=f"topic_{i}",
            )

    def test_topic_list_login_required_private(self):
        response = self.client.get(TOPIC_LIST_URL)
        self.assertEqual(response.status_code, 200)

    def test_topic_list(self):
        response = self.client.get(TOPIC_LIST_URL)
        topics = Topic.objects.all()[:5]
        self.assertEqual(
            list(topics),
            list(response.context["topic_list"]),
        )

    def test_topic_is_paginated(self):
        response = self.client.get(TOPIC_LIST_URL)
        self.assertTrue(response.context["is_paginated"])

    def test_number_of_topics_on_first_page(self):
        response = self.client.get(TOPIC_LIST_URL)
        self.assertEqual(
            len(response.context["topic_list"]),
            5
        )

    def test_number_of_topics_on_second_page(self):
        response = self.client.get(TOPIC_LIST_URL + "?page=2")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            len(response.context["topic_list"]),
            2
        )

    def test_context_contains_search_form(self):
        response = self.client.get(TOPIC_LIST_URL)
        self.assertIn("search_form", response.context)

    def test_searching(self):
        Topic.objects.create(name="Django")
        response = self.client.get(TOPIC_LIST_URL, {"name": "Django"})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.context["topic_list"]), 1)
        self.assertEqual(response.context["topic_list"][0].name, "Django")

    def test_empty_search_returns_full_list(self):
        response = self.client.get(TOPIC_LIST_URL, {"name": ""})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.context["topic_list"]), 5)

    def test_correct_template_used_list_view(self):
        response = self.client.get(TOPIC_LIST_URL)
        self.assertTemplateUsed(response, "tracker/topic_list.html")


class PrivateTopicCreateViewTests(TestCase):
    def setUp(self):
        user = get_user_model().objects.create_user(
            username="test_user",
            password="test_password"
        )
        self.client.force_login(user)
        topic = Topic.objects.create(
            name="test1",
        )

    def test_topic_create_login_required_private(self):
        response = self.client.get(TOPIC_CREATE_URL)
        self.assertEqual(response.status_code, 200)

    def test_topic_create_redirect_to_topic_list(self):
        response = self.client.post(TOPIC_CREATE_URL, {"name": "test2"})
        self.assertRedirects(
            response,
            TOPIC_LIST_URL
        )

    def test_new_topic_created(self):
        response = self.client.post(TOPIC_CREATE_URL, {"name": "test2"})
        self.assertEqual(response.status_code, 302)
        self.assertEqual(
            len(Topic.objects.all()),
            2
        )
        self.assertEqual(Topic.objects.all()[1].name, "test2")


    def test_correct_template_used_create_view(self):
        response = self.client.get(TOPIC_CREATE_URL)
        self.assertTemplateUsed(response, "tracker/topic_form.html")


class PrivateTopicUpdateViewTests(TestCase):
    def setUp(self):
        user = get_user_model().objects.create_user(
            username="test_user",
            password="test_password"
        )
        self.client.force_login(user)
        topic = Topic.objects.create(
            name="test",
        )

    def test_topic_update_login_required_private(self):
        response = self.client.get(TOPIC_UPDATE_URL)
        self.assertEqual(response.status_code, 200)


    def test_topic_update_redirects_to_topic_list(self):
        response = self.client.post(TOPIC_UPDATE_URL, {"name": "test2"})
        self.assertRedirects(
            response,
            TOPIC_LIST_URL
        )

    def test_topic_updated(self):
        self.assertEqual(Topic.objects.get(pk=1).name, "test")
        self.client.post(TOPIC_UPDATE_URL, {"name": "test2"})
        self.assertEqual(Topic.objects.get(pk=1).name, "test2")

    def test_topic_update_uses_correct_template(self):
        response = self.client.get(TOPIC_UPDATE_URL)
        self.assertTemplateUsed(response, "tracker/topic_form.html")



class PrivateTopicDeleteViewTests(TestCase):
    def setUp(self):
        user = get_user_model().objects.create_user(
            username="test_user",
            password="test_password"
        )
        self.client.force_login(user)
        topic = Topic.objects.create(
            name="test",
        )

    def test_topic_delete_login_required_private(self):
        response = self.client.get(TOPIC_DELETE_URL)
        self.assertEqual(response.status_code, 200)
