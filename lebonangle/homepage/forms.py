from django import forms

from .models import Item


class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ["title", "category", "description", "price", "picture"]
        labels = {
            "title": "Offer Title",
            "category": "Category",
            "description": "Description",
            "price": "Price",
            "picture": "Import 1 picture",
        }
