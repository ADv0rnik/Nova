from django.contrib import admin

from .models import Course, Module, Exercise


class ModuleInLine(admin.TabularInline):
    model = Module
    fields = ("title", "nm_exercises", "created_at")
    readonly_fields = ("created_at",)


class CourseAdmin(admin.ModelAdmin):
    inlines = [ModuleInLine]
    list_display = ("__str__", "created_at", "category")
    readonly_fields = ("created_at",)
    prepopulated_fields = {"slug": ("title",)}


class ExerciseInLine(admin.TabularInline):
    model = Exercise
    list_display = ("__str__", "ex_type", "points")
    readonly_fields = ("ex_type",)


class ModuleAdmin(admin.ModelAdmin):
    inlines = [ExerciseInLine]
    list_display = ("__str__", "created_at", "nm_exercises")
    prepopulated_fields = {"slug": ("title",)}


class ExerciseAdmin(admin.ModelAdmin):
    model = Exercise
    list_display = ("__str__", "created_at", "ex_type", "points")
    readonly_fields = ("ex_type", "created_at")
    prepopulated_fields = {"slug": ("title",)}


admin.site.register(Course, CourseAdmin)
admin.site.register(Module, ModuleAdmin)
admin.site.register(Exercise, ExerciseAdmin)
