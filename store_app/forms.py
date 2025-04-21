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

    def clean_description(self):
        description = self.cleaned_data['description']
        if len(description) < 5:
            raise forms.ValidationError("Описание должно содержать не менее 5 символов")
        return description


    def clean(self):
        cleaned_data = super().clean()
        name = cleaned_data.get('name')
        forbidden_words = ['синенькие', 'баллон', 'буряк']
        if forbidden_words:
            for word in forbidden_words:
                if word in name.lower():
                    raise forms.ValidationError(f"Наименование продукта не должно содержать слово '{word}'")
        return cleaned_data