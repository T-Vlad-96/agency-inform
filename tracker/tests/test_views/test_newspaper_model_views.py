from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse
from django.forms import Form

from tracker.models import Newspaper, Topic

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


class NewspaperListViewPrivateTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = get_user_model().objects.create_user(
            username="test_user",
            password="Test_Password123!"
        )
        number_of_newspapers = 7
        topic = Topic.objects.create(name="test_topic")
        publisher = get_user_model().objects.create_user(
            username="test_publisher",
            password="test_passwordABC1!"
        )
        for i in range(number_of_newspapers):
            newspaper = Newspaper.objects.create(
                title=f"test_Title_{i}",
                content="Text for the test newspaper."
            )
            newspaper.topics.add(topic)
            newspaper.publishers.add(publisher)

    def setUp(self):
        self.client.force_login(self.user)

    def test_newspaper_list_private(self):
        response = self.client.get(NEWSPAPER_LIST)
        self.assertEqual(
            response.status_code,
            200
        )

    def test_number_of_newspapers_on_first_page(self):
        response = self.client.get(NEWSPAPER_LIST)
        self.assertEqual(
            len(response.context["newspaper_list"]),
            5
        )

    def test_number_of_newspapers_on_second_page(self):
        response = self.client.get(NEWSPAPER_LIST + "?page=2")
        self.assertEqual(
            len(response.context["newspaper_list"]),
            2
        )

    def test_search_form_in_context(self):
        response = self.client.get(NEWSPAPER_LIST)
        self.assertIn("search_form", response.context)

    def test_search_form_is_django_forms_Form_instance(self):
        response = self.client.get(NEWSPAPER_LIST)
        self.assertIsInstance(
            response.context["search_form"],
            Form
        )

    def test_searching(self):
        response = self.client.get(
            NEWSPAPER_LIST, {"title": "test_Title_1"}
        )
        self.assertEqual(
            len(response.context["newspaper_list"]),
            1
        )
        self.assertEqual(
            response.context["newspaper_list"][0].title,
            "test_Title_1"
        )

    def test_empty_search_returns_full_list(self):
        response = self.client.get(NEWSPAPER_LIST, {"title": ""})
        self.assertEqual(
            len(response.context["newspaper_list"]),
            5
        )

    def test_newspaper_list_uses_correct_template(self):
        response = self.client.get(NEWSPAPER_LIST)
        self.assertTemplateUsed(
            response,
            "tracker/newspaper_list.html"
        )


class NewspaperCreateViewPrivateTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = get_user_model().objects.create_user(
            username="test_user",
            password="TestUserPassword123!"
        )
        cls.topic = Topic.objects.create(name="test_topic")
        cls.publisher = get_user_model().objects.create_user(
            username="test_publisher",
            password="TestPassword123!"
        )
        cls.data_for_newspaper_creating = {
            "title": "Test Title",
            "content": "Test content",
            "topics": [cls.topic.id],
            "publishers": [cls.publisher.id]
        }

    def setUp(self):
        self.client.force_login(self.user)

    def test_newspaper_create_private(self):
        response = self.client.get(NEWSPAPER_CREATE)
        self.assertEqual(
            response.status_code,
            200
        )

    def test_newspaper_created(self):
        response = self.client.post(
            NEWSPAPER_CREATE,
            self.data_for_newspaper_creating
        )
        self.assertEqual(
            len(Newspaper.objects.all()),
            1
        )
        self.assertEqual(
            Newspaper.objects.get(pk=1).title,
            "Test Title"
        )

    def test_newspaper_created_redirects(self):
        response = self.client.post(
            NEWSPAPER_CREATE,
            self.data_for_newspaper_creating
        )
        self.assertRedirects(
            response,
            NEWSPAPER_LIST
        )

    def test_newspaper_create_uses_correct_template(self):
        response = self.client.get(NEWSPAPER_CREATE)
        self.assertTemplateUsed(
            response,
            "tracker/newspaper_form.html"
        )
