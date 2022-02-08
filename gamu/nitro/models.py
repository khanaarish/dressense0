import email
from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Signup(models.Model):
    name = models.CharField(max_length=50)
    phone = models.CharField(max_length=12)
    password = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)

    def register(self):
        self.save()

    @staticmethod
    def get_by_email(email):
        try:
            return Signup.objects.get(email=email)
        except:
            return False

    def isExists(self):
        if Signup.objects.filter(email=self.email):
            return True

        return False
