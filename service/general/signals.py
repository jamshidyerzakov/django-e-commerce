import datetime

from django.utils.text import slugify


def pre_save_create_slug(sender, instance, *args, **kwargs):
    if not instance.slug:
        slug = slugify(instance.title)
        if not sender.objects.get_queryset().filter(slug=slug).exists():
            instance.slug = slug
        else:
            instance.slug = f"{slug}-{datetime.datetime.now().strftime('%Y%m%d%H%M%S')}"
