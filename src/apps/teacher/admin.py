from django.contrib import admin
from apps.teacher.models import Teacher, Specialty


# Register your models here.

@admin.register(Specialty)
class SpecialtyAdmin(admin.ModelAdmin):
    list_display = ("name",)


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ("user",)