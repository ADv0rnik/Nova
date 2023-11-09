from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Course, Module, Exercise, Category


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name",)
    prepopulated_fields = {"slug": ("name",)}


class ModuleInLine(admin.TabularInline):
    model = Module
    fields = ("title", "nm_exercises", "created_at")
    readonly_fields = ("created_at",)


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    inlines = [ModuleInLine]
    search_fields = ["title"]
    list_display = ("__str__", "created_at", "category")
    readonly_fields = ("created_at", "get_image",)
    prepopulated_fields = {"slug": ("title",)}

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.image.url} width="110" height="100">')

    get_image.short_description = "Image"


class ExerciseInLine(admin.TabularInline):
    model = Exercise
    list_display = ("__str__", "ex_type", "points")
    readonly_fields = ("ex_type",)


@admin.register(Module)
class ModuleAdmin(admin.ModelAdmin):
    inlines = [ExerciseInLine]
    list_display = ("__str__", "created_at", "nm_exercises")
    readonly_fields = ("get_image",)
    prepopulated_fields = {"slug": ("title",)}

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.image.url}> width="110" height="100">')

    get_image.short_description = "Image"


@admin.register(Exercise)
class ExerciseAdmin(admin.ModelAdmin):
    model = Exercise
    list_display = ("__str__", "created_at", "ex_type", "points")
    readonly_fields = ("ex_type", "created_at")
    prepopulated_fields = {"slug": ("title",)}
