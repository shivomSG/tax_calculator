from django import forms

class TaxForm(forms.Form):
    income = forms.DecimalField(label='Income', max_digits=10, decimal_places=2)
    deductions = forms.DecimalField(label='Deductions', max_digits=10, decimal_places=2)

    