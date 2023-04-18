from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm
from .models import User
from django import forms


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'Foydalanuvchi nomini kiriting'}))
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'Parolni kiriting'}))

    def __init__(self, *args, **kwargs):
        super(UserLoginForm, self).__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs["class"] = "form-control py-4"

    class Meta:
        model = User
        fields = ('username', 'password')


class UserRegistrationForm(UserCreationForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Ismingizni kiriting'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Familiyangizni kiriting'}))
    phone = forms.CharField(widget=forms.TextInput(attrs={"placeholder": "Telefon raqamingizni kiriting"}))
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Foydalanuvchi nomi'}))
    email = forms.CharField(widget=forms.EmailInput(attrs={'placeholder': 'Pochta manzil'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Parolni kiriting'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Parolni tasdiqlash'}))

    def __init__(self, *args, **kwargs):
        super(UserRegistrationForm, self).__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs["class"] = "form-control py-4"

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'phone', 'username', 'email', 'password1', 'password2')


class UserProfileForm(UserChangeForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'readonly': True}))
    email = forms.CharField(widget=forms.EmailInput(attrs={'readonly': True}))
    image = forms.ImageField(widget=forms.FileInput(), required=False)

    def __init__(self, *args, **kwargs):
        super(UserProfileForm, self).__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs["class"] = "form-control py-4"
        self.fields['image'].widget.attrs['class'] = "custom-file-input"

    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'phone', 'image')
