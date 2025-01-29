from django.test import TestCase

from tracker.models import Newspaper, Redactor, Topic


class TopicModelTest(TestCase):

    def test_topic_str(self):
        topic = Topic(name="test")
        self.assertEqual(str(topic), "test")

    def test_topic_ordering(self):
        self.assertEqual(Topic._meta.ordering, ["name"])


class RedactorModelTest(TestCase):
    pass


class NewspaperModelTest(TestCase):
    pass
