from django import forms
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm

from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(attrs={
            'class': (
                'w-full bg-bgDark border border-borderDark '
                'rounded-md px-3 py-1.5 text-sm text-white '
                'focus:outline-none focus:border-primary'
            ),
            'placeholder': 'Email'
        })
    )

    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ('username', 'email', 'password1', 'password2')
        widgets = {
            'username': forms.TextInput(attrs={
                'class': (
                    'w-full bg-bgDark border border-borderDark '
                    'rounded-md px-3 py-1.5 text-sm text-white '
                    'focus:outline-none focus:border-primary'
                ),
                'placeholder': 'Foydalanuvchi nomi'
            }),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        common_class = (
            'w-full bg-bgDark border border-borderDark '
            'rounded-md px-3 py-1.5 text-sm text-white '
            'focus:outline-none focus:border-primary'
        )

        self.fields['password1'].widget.attrs.update({
            'class': common_class,
            'placeholder': 'Parol'
        })

        self.fields['password2'].widget.attrs.update({
            'class': common_class,
            'placeholder': 'Parolni tasdiqlash'
        })


class CustomClearableFileInput(forms.widgets.ClearableFileInput):
    initial_text='Joriy rasm'
    input_text = 'Yangi rasm tanlash'
    clear_checkbox_label='Rasmni o\'chirish'


class EditProfileForm(forms.ModelForm):
    picture = forms.ImageField(
        required=False,
        widget=CustomClearableFileInput(
            attrs={
                'class': 'block w-full text-sm text-textMuted',
            },
        ),
        label='Profil rasmi'
    )

    class Meta:
        model = CustomUser
        fields = ('username', 'first_name', 'last_name', 'bio', 'picture', 'email')
    
        widgets = {
            "username": forms.TextInput(attrs={
                "class": "w-full bg-bgDark border border-boorderDark rounded-md px-3 py-2 text-sm focus:outline-none focus:border-primary"
            }),
            "email": forms.EmailInput(attrs={
                "class": "w-full bg-bgDark border border-borderDark rounded-md px-3 py-2 text-sm focus:outline-none focus:border-primary"
            }),
            "bio": forms.Textarea(attrs={
                "rows": 4,
                "class": "w-full bg-bgDark border border-borderDark rounded-md px-3 py-2 text-sm resize-none focus:outline-none focus:border-primary"
            }),
        } 


class CustomPasswordChangeForm(PasswordChangeForm):
    def __init__(self, user, *args, **kwargs):
        super().__init__(user, *args, **kwargs)

        for field in self.fields.values():
            field.widget.attrs.update({
                "class": "w-full bg-bgDark border border-borderDark rounded-md px-3 py-2 text-sm focus:outline-none focus:border-primary"
            })