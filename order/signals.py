from utils.generators import unique_id_generator


def pre_save_create_order_id(sender, instance, *args, **kwargs):
    if not instance.order_id:
        instance.order_id = unique_id_generator(instance)


def post_save_order(sender, instance, created, *args, **kwargs):
    if created:
        instance.total = instance.cart.total
        instance.save()
