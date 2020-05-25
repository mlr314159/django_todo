from django import forms
from .models import Item

class ItemForm(forms.ModelForm):

    class Meta:
        modal = Item
        fields = ('name', 'done')      