from django.core import validators
from django.db import models

# Create your models here.
SEX = (
    (1, "kobieta"),
    (2, "mężczyzna"),
)

ACTIVITY = (
    (1, "Raczej niska"),
    (2, "Umiarkowana aktywność"),
    (3, "Aktywny tryb życia"),
    (4, "Duża aktywność"),
)

class User(models.Model):
    name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    nickname = models.CharField(max_length=64)
    email = models.EmailField()

class UserData(models.Model):
    name = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    age = models.DateField(verbose_name='Wiek')
    hight = models.IntegerField(verbose_name='Wzrost')
    weight = models.IntegerField(verbose_name='Waga')
    sex = models.IntegerField(choices=SEX, verbose_name='Płeć')
    activity = models.IntegerField(choices=ACTIVITY, verbose_name='Aktywność fizyczna')


    def __str__(self):
        return self.age, self.hight, self.weight, self.sex, self.activity
