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
    pass


class NewspaperModelTest(TestCase):
    pass
