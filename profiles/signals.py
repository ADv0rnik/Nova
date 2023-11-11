import logging

from django.db.models.signals import post_save
from django.contrib.auth.models import User, Group
from .models import Profile
from django.dispatch import receiver


logger = logging.getLogger("asnova")
logger.event_source = __name__


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        # group_name = Group.objects.get(name='student')
        # instance.groups.add(group_name)
        Profile.objects.create(
            user=instance,
            first_name=instance.first_name,
            last_name=instance.last_name,
            email=instance.email,
        )
        logger.info(
            f"Profile created for {instance.username}",
            extra={
                "event_name": "create_profile",
                "event_source": logger.event_source,
            },
        )
