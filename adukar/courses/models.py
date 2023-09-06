from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.utils.translation import gettext_lazy as _


CAT_CHOICE = [
    ("life", "life"),
    ("computer", "computer")
]

EXERCISE_TYPE = [
    ("watch", "watch"),
    ("read", "read"),
    ("quiz", "quiz")
]


class Course(models.Model):
    title = models.CharField(
        _('Title'),
        max_length=250
    )
    num_lessons = models.IntegerField(
        _('Number Of Lessons'),
        default=0
    )
    description = models.TextField(
        _('Description'),
        max_length=250,
        null=True,
        blank=True
    )
    category = models.CharField(
        _('Category'),
        choices=CAT_CHOICE,
        max_length=100
    )
    ranking = models.DecimalField(
        _('Ranking'),
        max_digits=3,
        decimal_places=2,
        default=0
    )
    slug = models.SlugField(
        max_length=255,
        unique=True,
        db_index=True,
        verbose_name="URL"
    )
    created_at = models.DateTimeField(
        _('Created at'),
        auto_now_add=True
    )
    updated_at = models.DateTimeField(
        _('Updated at'),
        auto_now=True
    )

    def __str__(self):
        return f"{self.pk} - {self.title}"

    def get_absolute_url(self):
        return reverse('course', kwargs={'course_slug': self.slug})

    def get_module(self):
        return self.module_set.all()

    class Meta:
        verbose_name_plural = "Courses"


class Module(models.Model):
    course = models.ForeignKey(
        Course,
        on_delete=models.CASCADE
    )
    title = models.CharField(
        _('Title'),
        max_length=255,
    )
    nm_exercises = models.IntegerField(
        _('Number Of Exercises'),
        default=0
    )
    image = models.ImageField(
        _('Image'),
        default='default.png',
        null=True,
        blank=True
    )
    overview = models.TextField(
        _('Overview'),
        blank=True,
        null=True
    )
    slug = models.SlugField(
        max_length=255,
        unique=True,
        db_index=True,
        verbose_name="URL"
    )
    created_at = models.DateTimeField(
        _('Created at'),
        auto_now_add=True
    )
    updated_at = models.DateTimeField(
        _('Updated at'),
        auto_now=True
    )

    def __str__(self):
        return f"{self.pk} {self.title}"

    def get_absolute_url(self):
        return reverse('module', kwargs={'module_slug': self.slug})

    def get_exercise(self):
        return self.exercise_set.all()

    class Meta:
        verbose_name_plural = "Modules"


class Exercise(models.Model):
    module = models.ForeignKey(
        Module,
        on_delete=models.CASCADE
    )
    title = models.CharField(
        _('Title'),
        max_length=255,
    )
    description = models.TextField(
        _('Description'),
        max_length=250,
        null=True,
        blank=True
    )
    ex_type = models.CharField(
        _('Type Of Exercise'),
        choices=EXERCISE_TYPE
    )
    points = models.IntegerField(
        _("Points"),
        default=0
    )
    slug = models.SlugField(
        max_length=255,
        unique=True,
        db_index=True,
        verbose_name="URL"
    )
    created_at = models.DateTimeField(
        _('Created at'),
        auto_now_add=True
    )
    updated_at = models.DateTimeField(
        _('Updated at'),
        auto_now=True
    )

    def __str__(self):
        return f"{self.pk} {self.title}"

    def get_absolute_url(self):
        return reverse('exercise', kwargs={'exercise_slug': self.slug})

    class Meta:
        verbose_name_plural = "Exercises"
