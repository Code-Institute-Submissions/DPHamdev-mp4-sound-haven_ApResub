from django.db import models


class Category(models.Model):
    class Meta:
        verbose_name_plural = "Categories"

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Product(models.Model):
    category = models.ForeignKey('Category',
                                 null=True, blank=True,
                                 on_delete=models.SET_NULL)
    product_id = models.CharField(max_length=254, null=True, blank=True)
    name = models.CharField(max_length=254, null=True, blank=True)
    description = models.TextField()
    has_sizes = models.BooleanField(default=False, null=True, blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    rating = models.DecimalField(max_digits=6, decimal_places=1,
                                 null=True, blank=True)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    brand_title = models.CharField(max_length=254, null=True, blank=True)
    units_sold = models.IntegerField(default=0, null=False, blank=False)
    title = models.CharField(max_length=254)
    description_header = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name
