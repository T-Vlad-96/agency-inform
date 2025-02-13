from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

REDACTOR_LIST_URL = reverse("tracker:redactor_list")
REDACTOR_CREATE_URL = reverse("tracker:redactor_create")
REDACTOR_DETAIL_URL = reverse(
    "tracker:redactor_detail", kwargs={"pk": 1}
)
REDACTOR_UPDATE_URL = reverse(
    "tracker:redactor_update", kwargs={"pk": 1}
)
REDACTOR_DELETE_URL = reverse(
    "tracker:redactor_delete", kwargs={"pk": 1}
)

new_user_data = {
    "username": "test_user2",
    "password1": "TestPassword123!",
    "password2": "TestPassword123!",
    "first_name": "Test",
    "last_name": "User",
    "email": "test@example.com",
    "years_of_experience": 5,
}


class RedactorViewsPublicTests(TestCase):

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
    @classmethod
    def setUpTestData(cls):
        cls.user = get_user_model().objects.create_user(
            username="test",
            password="password"
        )
        number_of_users = 7
        for i in range(number_of_users):
            get_user_model().objects.create_user(
                username=f"user_{i}",
                password="password"
            )

    def setUp(self):
        self.client.force_login(self.user)

    def test_redactor_list_private(self):
        response = self.client.get(REDACTOR_LIST_URL)
        self.assertEquals(response.status_code, 200)

    def test_number_of_objects_on_first_page(self):
        response = self.client.get(REDACTOR_LIST_URL)
        self.assertEquals(
            len(response.context["redactor_list"]),
            5
        )

    def test_number_of_objects_on_second_page(self):
        response = self.client.get(REDACTOR_LIST_URL + "?page=2")
        self.assertEqual(
            len(response.context["redactor_list"]),
            3
        )

    def test_search_form_in_context(self):
        response = self.client.get(REDACTOR_LIST_URL)
        self.assertIn(
            "search_form",
            response.context
        )

    def test_searching(self):
        get_user_model().objects.create_user(
            username="admin",
            password="test_password"
        )
        response = self.client.get(
            REDACTOR_LIST_URL,
            {"username": "admin"}
        )
        self.assertEqual(
            len(response.context["redactor_list"]),
            1
        )
        self.assertEqual(
            response.context["redactor_list"][0].username,
            "admin"
        )

    def test_empty_search_returns_full_list(self):
        response = self.client.get(
            REDACTOR_LIST_URL,
            {"username": ""}
        )
        self.assertEqual(
            len(response.context["redactor_list"]),
            5
        )

    def test_redactor_list_uses_correct_template(self):
        response = self.client.get(REDACTOR_LIST_URL)
        self.assertTemplateUsed(
            response,
            "tracker/redactor_list.html"
        )


class RedactorCreateVIewPrivateTests(TestCase):
    def setUp(self):
        user = get_user_model().objects.create_user(
            username="test_user1",
            password="test_password"
        )
        self.client.force_login(user)

    def test_redactor_create_private(self):
        response = self.client.get(REDACTOR_CREATE_URL)
        self.assertEqual(response.status_code, 200)

    def test_redactor_create_view_redirect(self):
        response = self.client.post(
            REDACTOR_CREATE_URL,
            new_user_data
        )
        self.assertRedirects(
            response,
            REDACTOR_LIST_URL
        )

    def test_new_redactor_created(self):
        response = self.client.post(
            REDACTOR_CREATE_URL,
            new_user_data
        )
        self.assertEqual(
            len(get_user_model().objects.all()),
            2
        )
        self.assertEqual(
            get_user_model().objects.all()[1].username,
            "test_user2"
        )

    def test_redactor_create_uses_correct_template(self):
        response = self.client.get(REDACTOR_CREATE_URL)
        self.assertTemplateUsed(
            response,
            "tracker/redactor_form.html"
        )
