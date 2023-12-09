from django.db import models
from users.models import MyUser

# Create your models here.


class Item(models.Model):
    CLOTHING = "CLO"
    FURNITURE = "FUR"
    VEHICLE = "VEH"
    CATEGORY_CHOICES = [
        (CLOTHING, "Clothing"),
        (FURNITURE, "Furniture"),
        (VEHICLE, "Vehicle"),
    ]

    POSTED = "PO"
    SOLD = "SO"
    CANCELLED = "CA"
    ITEM_STATES = [(POSTED, "Posted"), (SOLD, "Sold"), (CANCELLED, "Cancelled")]

    title = models.CharField(max_length=200)
    category = models.CharField(max_length=3, choices=CATEGORY_CHOICES)
    description = models.CharField(max_length=2000)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    pub_date = models.DateTimeField()
    seller = models.ForeignKey(
        MyUser, on_delete=models.CASCADE, related_name="solditem"
    )
    buyer = models.ForeignKey(
        MyUser,
        on_delete=models.CASCADE,
        related_name="boughtitem",
        blank=True,
        null=True,
    )
    state = models.CharField(max_length=2, choices=ITEM_STATES)
    picture = models.ImageField(upload_to="item_photos/", blank=True, null=True)
