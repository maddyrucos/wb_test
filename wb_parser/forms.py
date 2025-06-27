from django import forms

class ProductSearchForm(forms.Form):
    query = forms.CharField(
        label='Название', required=False,
        widget=forms.TextInput(attrs={'placeholder': 'Название'})
    )
    min_price = forms.FloatField(
        label='Цена без скидки от', required=False,
        widget=forms.NumberInput(attrs={'placeholder': 'Цена без скидки от'})
    )
    max_price = forms.FloatField(
        label='Цена без скидки до', required=False,
        widget=forms.NumberInput(attrs={'placeholder': 'Цена без скидки до'})
    )
    min_discount_price = forms.FloatField(
        label='Цена со скидкой от', required=False,
        widget=forms.NumberInput(attrs={'placeholder': 'Цена со скидкой от'})
    )
    max_discount_price = forms.FloatField(
        label='Цена со скидкой до', required=False,
        widget=forms.NumberInput(attrs={'placeholder': 'Цена со скидкой до'})
    )
    min_rating = forms.FloatField(
        label='Рейтинг от', required=False,
        widget=forms.NumberInput(attrs={'placeholder': 'Рейтинг от'})
    )
    min_feedbacks = forms.IntegerField(
        label='Отзывов от', required=False,
        widget=forms.NumberInput(attrs={'placeholder': 'Отзывов от'})
    )