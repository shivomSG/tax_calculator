from django.shortcuts import render
from .forms import TaxForm
from decimal import Decimal

def calculate_tax(income, deductions):
    taxable_income = income - deductions
    if taxable_income <= Decimal('10000'):
        tax = Decimal('0')
    elif taxable_income <= Decimal('20000'):
        tax = taxable_income * Decimal('0.1')
    else:
        tax = Decimal('1000') + (taxable_income - Decimal('20000')) * Decimal('0.2')
    return max(Decimal('0'), tax)

def tax_view(request):
    if request.method == 'POST':
        form = TaxForm(request.POST)
        if form.is_valid():
            income = form.cleaned_data['income']
            deductions = form.cleaned_data['deductions']
            tax = calculate_tax(income, deductions)
            return render(request, 'taxapp/result.html', {'tax': tax})
    else:
        form = TaxForm()
    return render(request, 'taxapp/tax_form.html', {'form': form})
