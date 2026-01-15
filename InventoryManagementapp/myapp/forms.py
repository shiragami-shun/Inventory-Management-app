from django import forms
from models import Sale

class SaleForm(forms.ModelForm):
    class Meta:
        model = Sale
        fields = ["date", "product_id", "product_name", "price", "quantity"]
        widgets = {
            "date": forms.DateInput(attrs={"type": "date"})
        }