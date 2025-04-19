from django import forms

class ProductForm(forms.Form):
    name = forms.CharField(
        max_length=200,
        label="Наименование",
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите наименование товарной позиции'})
    )
    description = forms.CharField(
        label="Описание",
        widget=forms.Textarea(attrs={'class': 'form-control', 'row': 5, 'placeholder': 'Введите описание ТП'})
    )
    price = forms.FloatField(
        min_value=0,
        label="Цена",
        widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Введите цену товара'})
    )