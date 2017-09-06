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
TYPE = (
    (0, "Trener"),
    (1, "Dietetyk"),
    (2, "Klient"),
    (3, "Trener/Dietetyk"),
    (100, "Manager"),
)



class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    age = models.DateField(verbose_name='Wiek', null=True)
    height = models.FloatField(verbose_name='Wzrost', null=True)
    weight = models.FloatField(verbose_name='Waga', null=True)
    sex = models.IntegerField(choices=SEX, verbose_name='Płeć', null=True)
    activity = models.IntegerField(choices=ACTIVITY, verbose_name='Aktywność fizyczna', null=True)
    type = models.IntegerField(choices=TYPE, verbose_name="Rola", default=2)


    def __str__(self):
        return self.age, self.height, self.weight, self.sex, self.activity


@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)
    instance.userprofile.save()

