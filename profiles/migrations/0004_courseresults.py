# Generated by Django 4.2.5 on 2024-01-02 18:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("courses", "0006_remove_exercise_description_remove_module_content_and_more"),
        ("profiles", "0003_moduleresults"),
    ]

    operations = [
        migrations.CreateModel(
            name="CourseResults",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "passed",
                    models.BooleanField(
                        default=False,
                        help_text="the result of module taken",
                        verbose_name="Passed",
                    ),
                ),
                (
                    "course",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="courses.course"
                    ),
                ),
                (
                    "profile",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="course_results",
                        to="profiles.profile",
                    ),
                ),
            ],
            options={
                "verbose_name": "Course result",
                "verbose_name_plural": "Course results",
            },
        ),
    ]