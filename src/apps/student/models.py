from django.db import models
from apps.utils.models import BaseModel
from apps.users.models import User
from apps.teacher.models import Teacher
from apps.course.models import Group
# Create your models here.



class StatusChoices(models.TextChoices):

    HERE = "here", "Shu yerda"
    ABSENT = "absent", "Kelmagan"
    BECAUSE_OF = "because_of", "Sababli"



class StatusMessageChoices(models.TextChoices):

    NEW = "new", "Yangi"
    DONE = "done", "Hal qilindi"
    WAITING = "waiting", "Kutilmoqda..."



class Student(BaseModel):

    user = models.OneToOneField(User, on_delete=models.SET_NULL, null=True)
    total_ball = models.IntegerField(default=0)

    def __str__(self):
        return self.user
    


class StudentBallTransaction(BaseModel):

    teacher = models.ForeignKey(Teacher, on_delete=models.SET_NULL, null=True)
    student = models.ForeignKey(Student, on_delete=models.SET_NULL, null=True)
    ball = models.IntegerField(default=0)

    def __str__(self):
        return self.student
    

class StudentAttandance(BaseModel):

    teacher = models.ForeignKey(Teacher, on_delete=models.SET_NULL, null=True)
    student = models.ForeignKey(Student, on_delete=models.SET_NULL, null=True)
    group = models.ForeignKey(Group, on_delete=models.RESTRICT)
    status = models.CharField(max_length=20, choices=StatusChoices.choices)

    def __str__(self):
        return self.student
    


class StudentPayment(BaseModel):

    admin = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    student = models.ForeignKey(Student, on_delete=models.SET_NULL, null=True)
    group = models.ForeignKey(Group, on_delete=models.RESTRICT)
    amount = models.IntegerField(default=0)
    amount_for_month = models.DateField()

    def __str__(self):
        return f"{self.student} | {self.admin}"
    


class StudentMessages(BaseModel):

    student = models.ForeignKey(Student, on_delete=models.SET_NULL, null=True)
    status = models.CharField(max_length=20, choices=StatusMessageChoices.choices, default=StatusMessageChoices.NEW)
    text = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.student}"
    
