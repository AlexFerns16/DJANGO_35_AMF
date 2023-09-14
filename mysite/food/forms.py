from django import forms
from food.models import Item

class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['prod_code', 'for_user', 'item_name', 'item_desc', 'item_price', 'item_image']
