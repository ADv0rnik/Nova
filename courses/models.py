from PIL import Image

from django.db import models
from django.template.defaultfilters import slugify
from django.urls import reverse
from tinymce import models as tinymce_model
from django.utils.translation import gettext_lazy as _


class ExerciseType(models.Model):
    name = models.CharField(_("Type name"), max_length=20, null=False)

    def __str__(self):
        return f"{self.pk} - {self.name}"

    class Meta:
        verbose_name_plural = _("Exercise types")


class Category(models.Model):
    name = models.CharField(_("Category name"), max_length=100)
    slug = models.SlugField(unique=True, verbose_name="URL")

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"


class Course(models.Model):
    title = models.CharField(_("Title"), max_length=255)
    num_lessons = models.IntegerField(_("Number Of Lessons"), default=0)
    description = models.TextField(_("Description"), null=True, blank=True)
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name="course_category"
    )
    image = models.ImageField(_("Image"), default="default.png", upload_to="course/")
    ranking = models.DecimalField(
        _("Ranking"), max_digits=3, decimal_places=2, default=0
    )
    slug = models.SlugField(
        max_length=255, unique=True, db_index=True, verbose_name="URL"
    )
    created_at = models.DateTimeField(_("Created at"), auto_now_add=True)
    updated_at = models.DateTimeField(_("Updated at"), auto_now=True)

    def __str__(self):
        return f"{self.pk} - {self.title}"

    def get_absolute_url(self):
        return reverse("course", kwargs={"course_slug": self.slug})

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        img = Image.open(self.image.path)
        if img.height > 300 or img.width > 300:
            output_size = (400, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)

    class Meta:
        verbose_name = "Course"
        verbose_name_plural = "Courses"


class Module(models.Model):
    course = models.ForeignKey(
        Course, on_delete=models.CASCADE, related_name="course_module"
    )
    title = models.CharField(
        _("Title"),
        max_length=255,
    )
    nm_exercises = models.IntegerField(_("Number Of Exercises"), default=0)
    image = models.ImageField(
        _("Image"),
        default="default.png",
        null=True,
        blank=True,
        upload_to="modules/%Y/%m/%d",
    )
    description = models.TextField(_("Description"), null=True, blank=True)
    slug = models.SlugField(
        max_length=255, unique=True, db_index=True, verbose_name="URL"
    )
    created_at = models.DateTimeField(_("Created at"), auto_now_add=True)
    updated_at = models.DateTimeField(_("Updated at"), auto_now=True)

    def __str__(self):
        return f"{self.pk} {self.title}"

    def get_absolute_url(self):
        return reverse("module", kwargs={"module_slug": self.slug})

    def get_exercise(self):
        return self.exercise_module.all()

    @property
    def total_score(self):
        exercises = self.get_exercise()
        total_score = sum([exercise.points for exercise in exercises])
        return total_score

    def save(self, *args, **kwargs):
        if not self.pk:
            self.slug = slugify(self.title)
        super(Module, self).save(*args, **kwargs)

    class Meta:
        verbose_name = _("Module")
        verbose_name_plural = _("Modules")
        ordering = ["course"]


class Exercise(models.Model):
    module = models.ForeignKey(
        Module, on_delete=models.CASCADE, related_name="exercise_module"
    )
    title = models.CharField(
        _("Title"),
        max_length=255,
    )
    content = tinymce_model.HTMLField(_("Content"), null=True, blank=True)
    ex_type = models.ForeignKey(ExerciseType, on_delete=models.CASCADE)
    points = models.IntegerField(_("Points"), default=0)
    slug = models.SlugField(
        max_length=255, unique=True, db_index=True, verbose_name="URL"
    )
    created_at = models.DateTimeField(_("Created at"), auto_now_add=True)
    updated_at = models.DateTimeField(_("Updated at"), auto_now=True)

    def __str__(self):
        return f"{self.pk} {self.title}"

    def get_absolute_url(self):
        return reverse("exercise", kwargs={"exercise_slug": self.slug})

    class Meta:
        verbose_name = _("Exercise")
        verbose_name_plural = _("Exercises")
