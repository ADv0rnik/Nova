from django.contrib import admin
from .models import Profile, ModuleResults


class ModuleResultsInline(admin.TabularInline):
    model = ModuleResults
    list_display = ("__str__", "score", "created_at")
    readonly_fields = ("created_at",)


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ("__str__", "email", "is_teacher")
    inlines = [ModuleResultsInline]
    readonly_fields = ("created_at", "updated_at")


admin.site.register(ModuleResults)
