from django.db import models
from django_countries.fields import CountryField


class CustomerAddress(models.Model):
    """Representation of an address for customers"""
    customer = models.ForeignKey('accounts.Customer',
                                 on_delete=models.PROTECT,
                                 related_name='customer_addresses'
                                 )
    address_line_1 = models.CharField(max_length=120, verbose_name="Address line")
    address_line_2 = models.CharField(max_length=120, verbose_name="Second address line (optional)", blank=True)
    country = CountryField(multiple=False, verbose_name="Country of a customer")
    city = models.CharField(max_length=120, verbose_name="City of a customer")
    state = models.CharField(max_length=120, verbose_name="State of a customer")
    postal_code = models.CharField(max_length=120, verbose_name="Postal code of a customer")

    def __str__(self):
        return f"Customer - {self.customer.__str__()!r}, address - {self.address_line_1!r}."

    def get_full_address(self):
        return "{customer_name}\n{line1}\n{line2}\n{city}\n{state}, {postal}\n{country}".format(
            customer_name=self.customer.__str__(),
            line1=self.address_line_1,
            line2=self.address_line_2 or "",
            city=self.city,
            state=self.state,
            postal=self.postal_code,
            country=self.country
        )

    class Meta:
        verbose_name_plural = 'Customer Addresses'
        verbose_name = 'Customer Address'
        ordering = ('customer',)


class SellerAddress(models.Model):
    """Representation of an address for sellers"""
    seller = models.ForeignKey('accounts.Seller',
                               on_delete=models.PROTECT,
                               related_name='seller_addresses'
                               )
    address_line_1 = models.CharField(max_length=120, verbose_name="Address line")
    address_line_2 = models.CharField(max_length=120, verbose_name="Second address line (optional)", blank=True)
    country = CountryField(multiple=False, verbose_name="Country of a customer")
    city = models.CharField(max_length=120, verbose_name="City of a customer")
    state = models.CharField(max_length=120, verbose_name="State of a customer")
    postal_code = models.CharField(max_length=120, verbose_name="Postal code of a customer")

    def __str__(self):
        return f"Seller - {self.seller.__str__()!r}, address - {self.address_line_1!r}."

    def get_full_address(self):
        return "{seller_name}\n{line1}\n{line2}\n{city}\n{state}, {postal}\n{country}".format(
            seller_name=self.seller.__str__(),
            line1=self.address_line_1,
            line2=self.address_line_2 or "",
            city=self.city,
            state=self.state,
            postal=self.postal_code,
            country=self.country
        )

    class Meta:
        verbose_name_plural = 'Seller Addresses'
        verbose_name = 'Seller Address'
        ordering = ('seller',)
