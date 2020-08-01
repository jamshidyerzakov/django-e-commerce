from django.contrib.contenttypes.models import ContentType
from django.db import models
from django.template.defaultfilters import slugify
from djmoney.models.fields import MoneyField
from django.contrib.contenttypes.fields import GenericForeignKey

from accounts.models import Admin, Moderator, Seller


class ProductManager(models.Manager):
    def all(self, **kwargs):
        return self.filter(active=True, **kwargs)


class Product(models.Model):

    limit_user_types = models.Q(app_label="accounts", model="seller") | \
                       models.Q(app_label="accounts", model="admin") | \
                       models.Q(app_label="accounts", model="moderator")
    content_type = models.ForeignKey(
        ContentType,
        on_delete=models.PROTECT,
        limit_choices_to=limit_user_types,
        related_name="products",
        verbose_name="Type of user"
    )
    object_id = models.PositiveIntegerField(verbose_name="Id of a user")

    owner = GenericForeignKey('content_type', 'object_id')
    category = models.ForeignKey(
        'category.Category',
        on_delete=models.PROTECT,
        related_name="products",
        verbose_name="Category of a product"
    )

    price = MoneyField(
        max_digits=12,
        decimal_places=2,
        default_currency='UZS',
        verbose_name='Price of a product'
    )

    slug = models.SlugField(
        max_length=127,
        unique=True,
        blank=True,
        verbose_name="Slug (If no slug title will be slugified)"
    )

    title = models.CharField(max_length=127, verbose_name="Title of a product")
    description = models.TextField(verbose_name="Description of a product")
    product_fabricator = models.CharField(max_length=127, verbose_name="Fabricator of a product", blank=True)

    views = models.PositiveIntegerField(default=0, verbose_name="Number of views of a product")
    amount = models.PositiveIntegerField(default=0, verbose_name="Amount of a product")

    size = models.CharField(max_length=10, verbose_name="Size of a product", blank=True)
    color = models.CharField(max_length=63, verbose_name="Color of a product", blank=True)

    active = models.BooleanField(default=True, verbose_name="Designates whether a product active or not")
    created_at = models.DateTimeField(auto_now_add=True)

    objects = ProductManager()

    class Meta:
        ordering = ('title',)
        verbose_name = 'Product'
        verbose_name_plural = 'Products'

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)

    def __str__(self):
        return self.title


class ProductImage(models.Model):
    product = models.ForeignKey('Product', on_delete=models.PROTECT)
    image = models.ImageField(upload_to='images/products', verbose_name="Image of a product")

    def __str__(self):
        return self.image.__str__().split("/")[-1]  # get name of the image
