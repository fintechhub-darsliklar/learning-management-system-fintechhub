from django.contrib import admin
from apps.student.models import Student, StudentBallTransaction, StudentAttandance, StudentPayment, StudentMessages


# Register your models here.

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ("user",)


@admin.register(StudentBallTransaction)
class StudentBallTransactionAdmin(admin.ModelAdmin):
    list_display = ("student",)


@admin.register(StudentAttandance)
class StudentAttandanceAdmin(admin.ModelAdmin):
    list_display = ("student",)


@admin.register(StudentPayment)
class StudentPaymentAdmin(admin.ModelAdmin):
    list_display = ("student",)


@admin.register(StudentMessages)
class StudentMessagesAdmin(admin.ModelAdmin):
    list_display = ("student",)