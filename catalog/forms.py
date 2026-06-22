from django import forms

class SelectionForm(forms.Form):
    flow_rate = forms.DecimalField(
        label='Расход жидкости (м³/ч)',
        min_value=0.01,
        decimal_places=2,
        max_digits=10,
        widget=forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'})
    )
    pressure = forms.DecimalField(
        label='Рабочее давление (бар)',
        min_value=0.01,
        decimal_places=2,
        max_digits=10,
        widget=forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'})
    )
