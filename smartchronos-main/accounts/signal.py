from django.db.models.signals import pre_save, post_save, pre_delete, post_delete
from django.dispatch import receiver
from .models import CustomUser, UserGroup

@receiver(pre_save, sender=CustomUser)
def registration_pre_save(sender, instance, **kwargs):
    print("SEU DADOS JÁ ESTÁ NO DB")

@receiver(post_save, sender=CustomUser)
def registration_pre_save(sender, instance, **kwargs):
    print("SEU DADOS JÁ ESTÁ NO DB")

@receiver(pre_delete, sender=CustomUser)
def registration_pre_save(sender, instance, **kwargs):
    print("SEU DADOS JÁ ESTÁ NO DB")

@receiver(post_delete, sender=CustomUser)
def registration_pre_save(sender, instance, **kwargs):
    print("SEU DADOS JÁ ESTÁ NO DB")

@receiver(pre_save, sender=UserGroup)
def group_pre_save(sender, instance, **kwargs):
    print("SEU DADOS JÁ ESTÁ NO DB")

@receiver(post_save, sender=UserGroup)
def registration_pre_save(sender, instance, **kwargs):
    print("SEU DADOS JÁ ESTÁ NO DB")

@receiver(pre_delete, sender=UserGroup)
def registration_pre_save(sender, instance, **kwargs):
    print("SEU DADOS JÁ ESTÁ NO DB")

@receiver(post_delete, sender=UserGroup)
def registration_pre_save(sender, instance, **kwargs):
    print("SEU DADOS JÁ ESTÁ NO DB")
