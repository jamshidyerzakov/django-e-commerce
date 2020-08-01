from django.db import models
from django.utils.text import slugify


class Category(models.Model):
    """Categorizing posts"""
    title = models.CharField(max_length=128, verbose_name="Title")
    description = models.TextField(verbose_name="Description")
    slug = models.SlugField(max_length=128, unique=True, blank=True)
    children_categories = models.ForeignKey(
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
        return self.title[:20]

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)
