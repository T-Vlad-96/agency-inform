from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from django.test import TestCase

from tracker.models import Newspaper, Redactor, Topic


class TopicModelTest(TestCase):

    def test_topic_str(self):
        topic = Topic(name="test")
        self.assertEqual(str(topic), "test")

    def test_topic_ordering(self):
        self.assertEqual(Topic._meta.ordering, ["name"])

    def test_topic_object_name_is_unique(self):
        topic = Topic.objects.create(name="test")
        topic2 = Topic(name="test")

        with self.assertRaises(ValidationError):
            topic2.full_clean()


class RedactorModelTest(TestCase):

    def test_redactor_str(self):
        redactor = Redactor(username="test")
        self.assertEqual(str(redactor), "test")

    def test_redactor_ordering(self):
        self.assertEqual(Redactor._meta.ordering, ["username"])

    def test_redactor_years_of_experience(self):
        username = "test"
        password = "Abc12345"
        years_of_experience = 20
        self.redactor = get_user_model().objects.create_user(
            username=username,
            password=password,
            years_of_experience=years_of_experience,
        )
        self.assertEqual(self.redactor.username, username)
        self.assertTrue(self.redactor.check_password(password))
        self.assertEqual(self.redactor.years_of_experience, years_of_experience)


class NewspaperModelTest(TestCase):
    pass
