from django import forms
from django.contrib.auth.forms import UserCreationForm
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
                'placeholder': 'Username'
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
            'placeholder': 'Password'
        })

        self.fields['password2'].widget.attrs.update({
            'class': common_class,
            'placeholder': 'Confirm password'
        })



class EditProfileForm(forms.ModelForm):
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
            "picture": forms.ClearableFileInput(attrs={
                "class": "text-sm text-textMuted"
            })
        } 