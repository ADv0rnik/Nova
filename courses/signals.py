import os
import logging

from django.db.models.signals import post_delete
from django.dispatch import receiver
from courses.models import Course


logger = logging.getLogger("asnova")
logger.event_source = __name__


@receiver(post_delete)
def auto_delete_file_on_delete(sender, instance, **kwargs):
    list_of_models = ("Course", "Module")
    if sender.__name__ in list_of_models:
        if instance.image:
            if os.path.isfile(instance.image.path):
                os.remove(instance.image.path)
    else:
        logger.debug(
            f"Error while delete image from {sender.__name__}",
            extra={
                "event_name": "auto_delete_file_on_delete",
                "event_source": logger.event_source,
            },
        )
