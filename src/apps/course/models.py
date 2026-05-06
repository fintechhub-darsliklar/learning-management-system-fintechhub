from django.db import models
from apps.utils.models import BaseModel
from apps.teacher.models import Specialty, Teacher
# Create your models here.


class GroupDays(models.TextChoices):
    TOQKUNLAR = 'toqkunlar', "Duyshanba/Chorshanba/Juma"
    JUFTKUNLAR = 'juftkunlar', "Seyshanba/Payshanba/Shanba"



class Course(BaseModel):

    specialty = models.ForeignKey(Specialty, on_delete=models.RESTRICT)
    name = models.CharField(max_length=50)
    description = models.TextField(blank=True, null=True)
    monthly_payment = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.name}"
    
    class Meta:
        verbose_name = "Kurs"
        verbose_name_plural = "Kurslar"
    


class Room(BaseModel):
    name = models.CharField(max_length=50)
    description = models.TextField(blank=True, null=True)
    number = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.name}"
    
    class Meta:
        verbose_name = "Xona"
        verbose_name_plural = "Xonalar"
    

class Group(BaseModel):
    cource = models.ForeignKey(Course, on_delete=models.RESTRICT)
    teacher = models.ForeignKey(Teacher, on_delete=models.RESTRICT)
    room = models.ForeignKey(Room, on_delete=models.SET_NULL, null=True)
    students = models.ManyToManyField("student.Student", blank=True)
    name = models.CharField(max_length=50)
    description = models.TextField(blank=True, null=True)
    start_time = models.TimeField()
    end_time = models.TimeField()
    start_date= models.DateField()
    end_date= models.DateField()
    lesson_days = models.CharField(max_length=30, choices=GroupDays.choices)

    def __str__(self):
        return f"{self.name}"
    
    class Meta:
        verbose_name = "Gurux"
        verbose_name_plural = "Guruxlar"