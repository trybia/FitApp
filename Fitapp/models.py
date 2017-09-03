from django.contrib.auth.models import User
from django.core import validators
from django.db import models

# Create your models here.
from django.db.models.signals import post_save
from django.dispatch import receiver

SEX = (
    (0, "brak danych"),
    (1, "kobieta"),
    (2, "mężczyzna"),
)

ACTIVITY = (
    (0, "Brak danych"),
    (1, "Raczej niska"),
    (2, "Umiarkowana aktywność"),
    (3, "Aktywny tryb życia"),
    (4, "Duża aktywność"),
)



class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    age = models.DateField(verbose_name='Wiek', null=True)
    hight = models.IntegerField(verbose_name='Wzrost', null=True)
    weight = models.IntegerField(verbose_name='Waga', null=True)
    sex = models.IntegerField(choices=SEX, verbose_name='Płeć', null=True)
    activity = models.IntegerField(choices=ACTIVITY, verbose_name='Aktywność fizyczna', null=True)


    def __str__(self):
        return self.age, self.hight, self.weight, self.sex, self.activity


@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)
    instance.userprofile.save()