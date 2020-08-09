from django.db import models
from django.db.models.signals import pre_save

from service.general.signals import pre_save_create_slug


class Category(models.Model):
    """Categorizing posts"""
    title = models.CharField(max_length=128, verbose_name="Title")
    description = models.TextField(verbose_name="Description")
    slug = models.SlugField(
        max_length=128,
        help_text="optional (title will be slugified) or write UNIQUE slug",
        unique=True,
        blank=True
    )
    parent_category = models.ForeignKey(
        'self',
        null=True,
        blank=True,
        on_delete=models.PROTECT,
        verbose_name="Children categories",
        related_name="children",
    )

    class Meta:
        ordering = ('title',)
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return str(self.slug)


pre_save.connect(pre_save_create_slug, sender=Category)
