from django import forms


class OrderForm(forms.Form):
    phone = forms.CharField(max_length=200, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': "Telefon raqamingizni qoldiring"}))
