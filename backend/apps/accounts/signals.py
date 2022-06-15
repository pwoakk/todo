from django.db.models.signals import post_save
from django.dispatch import receiver

from backend.apps.accounts.models import User, DirectorProfile, WorkerProfile, ManagerProfile


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        if instance.role == User.ROLE_MANAGER:
            ManagerProfile.objects.create(user=instance)
        elif instance.role == User.ROLE_DIRECTOR:
            DirectorProfile.objects.create(user=instance)
        else:
            WorkerProfile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    if instance.role == User.ROLE_MANAGER:
        instance.managerprofile.save()
    elif instance.role == User.ROLE_DIRECTOR:
        instance.directorprofile.save()
    else:
        instance.workerprofile.save()
