from django import forms
from .models import Product

FORBIDDEN_WORDS = [
    'казино', 'криптовалюта', 'крипта', 'биржа',
    'дешево', 'бесплатно', 'обман', 'полиция', 'радар'
]

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'price']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите название продукта'
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 4,
                'placeholder': 'Введите описание продукта'
            }),
            'price': forms.NumberInput(attrs={
                'class': 'form-control',
                'step': '0.01'
            }),
        }

    def clean_name(self):
        name = self.cleaned_data.get('name')
        if name:
            self._check_forbidden_words(name, 'name')
        return name

    def clean_description(self):
        description = self.cleaned_data.get('description')
        if description:
            self._check_forbidden_words(description, 'description')
        return description

    def _check_forbidden_words(self, text, field_name):
        text_lower = text.lower()
        for word in FORBIDDEN_WORDS:
            if word in text_lower:
                field_label = 'Название' if field_name == 'name' else 'Описание'
                raise forms.ValidationError(
                    f'{field_label} содержит запрещённое слово: "{word}"'
                )

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'price']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Общие стили для всех полей
        common_attrs = {
            'class': 'form-control',
            'placeholder': 'Введите значение...'
        }

        # Индивидуальные стили для каждого поля
        self.fields['name'].widget.attrs.update({
            **common_attrs,
            'placeholder': 'Название продукта',
            'autofocus': 'autofocus'
        })

        self.fields['description'].widget.attrs.update({
            **common_attrs,
            'placeholder': 'Описание продукта',
            'rows': '4',
            'class': 'form-control form-control-lg'
        })

        self.fields['price'].widget.attrs.update({
            **common_attrs,
            'placeholder': '0.00',
            'step': '0.01',
            'min': '0',
            'class': 'form-control'
        })

    def clean_price(self):
        price = self.cleaned_data.get('price')

        if price is None:
            return price

        if price < 0:
            raise forms.ValidationError(
                'Цена не может быть отрицательной. Пожалуйста, введите положительное число или ноль.'
            )

        return price