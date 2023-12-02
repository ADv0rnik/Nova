import pytest
from django.test import TestCase, Client

from courses.models import Category, Course


@pytest.fixture(autouse=True)
def use_dummy_cache_backend(settings):
    settings.SECRET_KEY = "748_59$9-hx*o5klljprr)3y^9=q@5#+i97zm2)&eo#8+mhf_s"
    settings.DEBUG = True


class CategoryTestCase(TestCase):
    @pytest.mark.django_db
    def setUp(self) -> None:
        self.client = Client()
        self.category = Category.objects.create(name="Biology", slug="biology")

    def test_category_name(self):
        return self.assertEqual(self.category.name, "Biology")

    def test_category_slug(self):
        return self.assertEqual(self.category.slug, "biology")


class CourseTestCase(TestCase):

    @pytest.mark.django_db
    def setUp(self):
        self.client = Client()
        self.category = Category.objects.create(name="Biology", slug="biology")
        self.course = Course.objects.create(
            title="Cell biology", num_lessons=10, category=self.category
        )

    def test_course_title(self):
        return self.assertEqual(self.course.title, "Cell biology")

    def test_course_category(self):
        return self.assertEqual(self.course.category.name, self.category.name)

    def test_str_call(self):
        return self.assertEqual(
            self.course.__str__(), f"{self.course.pk} - {self.course.title}"
        )

    def test_request(self):
        resp = self.client.get("/courses")
        return self.assertEqual(resp.status_code, 301)
