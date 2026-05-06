from django.db import models
from apps.utils.models import BaseModel
from apps.users.models import User
# Create your models here.


class Specialty(BaseModel):

    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
    


class Teacher(BaseModel):

    user = models.OneToOneField(User, on_delete=models.SET_NULL, null=True)
    specialty = models.ForeignKey(Specialty, on_delete=models.SET_NULL, null=True)
    celery = models.IntegerField(default=0)

    def __str__(self):
        return self.user
    

    