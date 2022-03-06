import uuid

from django.db import models
from django.db.models import Sum
from django.conf import settings

from services.models import Service


# Create your models here.

class Order(models.Model):
    order_number = models.CharField(max_length=32, null=False, editable=False)
    full_name = models.CharField(max_length=50, null=False, blank=False)
    email = models.EmailField(max_length=254, null=False, blank=False)
    phone_number = models.CharField(max_length=20, null=False, blank=False)
    country = models.CharField(max_length=40, null=False, blank=False)
    postcode = models.CharField(max_length=20, null=True, blank=True)
    town_or_city = models.CharField(max_length=40, null=False, blank=False)
    street_address1 = models.CharField(max_length=80, null=False, blank=False)
    street_address2 = models.CharField(max_length=80, null=True, blank=True)
    county = models.CharField(max_length=80, null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)
    discount = models.DecimalField(max_digits=6, decimal_places=2, null=False, default=0)
    order_total = models.DecimalField(
        max_digits=10, decimal_places=2, null=False, default=0)
    net_total = models.DecimalField(
        max_digits=10, decimal_places=2, null=False, default=0)

    def __generate_order_number(self):
        """
        Generate random and unique order number with UUID
        """
        return uuid.uuid4().hex.upper()

    def update_total(self):
        """
        Update net total each time a line item is added
        """
        self.order_total = self.lineitems.aggregate(Sum(
            'lineitem_total'))['lineitem_total__sum']

        if self.quantity > 1:
            self.discount = self.order_total * (settings.COMBINATION_DISCOUNT_PERCENTAGE / 100)
            self.net_total = self.order_total - self.discount
        else:
            self.discount = 0
            self.net_total = self.order_total

        self.save()

    def save(self, *args, **kwargs):
        """
        Override original save method to set ordernumber
        if it has not already been set
        """
        if not self.order_number:
            self.order_number = self._generate_order_number()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.order_number


class OrderLineItem(models.Model):
    order = models.ForeignKey(
        Order, null=False, blank=False, on_delete=models.CASCADE, related_name='lineitems')
    service = models.ForeignKey(
        Service, null=False, blank=False, on_delete=models.CASCADE)
    quantity = models.IntegerField(
        null=False, blank=False, default=0)
    lineitem_total = models.DecimalField(
        max_digits=6, decimal_places=2, null=False, blank=False, editable=False)

    def save(self, *args, **kwargs):
        """
        Override original save method to set lineitem total
        and update the order total
        """
        self.lineitem_total = self.service.price * self.quantity
        super().save(*args, **kwargs)

    def __str__(self):
        return f'SKU { self.service.sku} on order {self.order.order_number}'
