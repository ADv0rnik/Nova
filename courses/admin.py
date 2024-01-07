from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Course, Module, Exercise, Category, ExerciseType


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name",)
    prepopulated_fields = {"slug": ("name",)}


@admin.register(ExerciseType)
class ExerciseTypeAdmin(admin.ModelAdmin):
    list_display = ("name",)


class ModuleInLine(admin.TabularInline):
    model = Module
    fields = ("title", "nm_exercises")
    readonly_fields = ("created_at",)


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    inlines = [ModuleInLine]
    search_fields = ["title"]
    list_display = ("__str__", "created_at", "category")
    readonly_fields = (
        "created_at",
        "get_image",
    )
    prepopulated_fields = {"slug": ("title",)}

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.image.url} width="110" height="100">')

    get_image.short_description = "Image"


class ExerciseInLine(admin.TabularInline):
    model = Exercise
    list_display = ("__str__", "ex_type", "points")
    prepopulated_fields = {"slug": ("title",)}


@admin.register(Module)
class ModuleAdmin(admin.ModelAdmin):
    inlines = [ExerciseInLine]
    list_display = ("__str__", "created_at", "total_score", "nm_exercises")
    readonly_fields = ("get_image",)
    prepopulated_fields = {"slug": ("title",)}

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.image.url} width="110" height="100">')

    get_image.short_description = "Image"


@admin.register(Exercise)
class ExerciseAdmin(admin.ModelAdmin):
    model = Exercise
    list_display = ("__str__", "created_at", "ex_type", "module", "points")
    readonly_fields = ("created_at",)
    prepopulated_fields = {"slug": ("title",)}
