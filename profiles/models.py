from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import gettext_lazy as _

from courses.models import Module, Course


class Profile(models.Model):
    user = models.ForeignKey(User, verbose_name=_("user"), on_delete=models.CASCADE)
    first_name = models.CharField(_("First Name"), max_length=50)
    last_name = models.CharField(_("Last Name"), max_length=50)
    email = models.EmailField(
        _("Email"), max_length=100, unique=True, blank=True, null=True
    )
    nickname = models.CharField(_("nickname"), max_length=100, blank=True, null=True)
    photo = models.ImageField(
        _("Photo"), upload_to="profiles/%Y/%m/%d", default="default_prof.png"
    )
    is_teacher = models.BooleanField(_("Is teacher"), default=False)
    occupation = models.CharField(
        _("occupation"), blank=True, null=True, max_length=100
    )
    created_at = models.DateTimeField(_("Created at"), db_index=True, auto_now_add=True)
    updated_at = models.DateTimeField(_("Updated at"), auto_now=True)

    def __str__(self):
        return f"Profile: {self.pk} {self.first_name} {self.last_name}"

    class Meta:
        verbose_name = _("Profile")
        verbose_name_plural = _("Profiles")
        ordering = ["last_name"]


class ModuleResults(models.Model):
    module = models.ForeignKey(Module, on_delete=models.CASCADE, related_name="results")
    score = models.DecimalField(_("Score"), max_digits=3, decimal_places=2, default=0)
    profile = models.ForeignKey(
        Profile, on_delete=models.CASCADE, related_name="module_results"
    )
    passed = models.BooleanField(
        _("Passed"), default=False, help_text="the result of module taken"
    )
    created_at = models.DateTimeField(_("Created at"), auto_now_add=True)

    def __str__(self):
        return f"{self.pk} - {self.module}: {self.passed}"

    class Meta:
        verbose_name = _("Module Result")
        verbose_name_plural = _("Module Results")


class CourseResults(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    profile = models.ForeignKey(
        Profile, on_delete=models.CASCADE, related_name="course_results"
    )
    passed = models.BooleanField(
        _("Passed"), default=False, help_text="the result of module taken"
    )

    def __str__(self):
        return f"{self.course}: {self.passed}"

    class Meta:
        verbose_name = _("Course result")
        verbose_name_plural = _("Course results")
