from django.core.exceptions import ValidationError
from django.forms import ModelForm, BooleanField

from catalog.models import Product
FORBIDEN_WORDS = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар']

class StileFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for fild_name, fild in self.fields.items():
            if isinstance(fild, BooleanField):
                fild.widget.attrs['class'] = "form-check-input"
            else:
                fild.widget.attrs['class'] = "form-control"


class ProductForm(StileFormMixin,ModelForm):
    class Meta:
        model = Product
        fields = "__all__"


    def clean_price(self):
        price = self.cleaned_data["price"]
        if price <= 0:
            raise ValidationError("Цена должна быть положительной")
        return price


    def clean_name(self):
        name = self.cleaned_data["name"]
        if name.lower() in FORBIDEN_WORDS:
            raise ValidationError("Используется запрещенное слово, измените содержимое")
        return name

    def clean_description(self):
        description = self.cleaned_data['description']
        for word in FORBIDEN_WORDS:
            if word in description.lower():
                raise ValidationError("Используется запрещенное слово, измените содержимое")
        return description