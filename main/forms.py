from django import forms

from .models import Post, Tags



class PostCreateForm(forms.ModelForm):
    tags = forms.ModelMultipleChoiceField(
        queryset=Tags.objects.all(),
        required=True,
        widget=forms.SelectMultiple(attrs={
            'class': 'w-full bg-bgDark border border-borderDark rounded-md px-3 py-2 text-sm focus:outline-none focus:border-primary'
        })
    )

    class Meta:
        model = Post
        fields = (
            'body', 'code', 'tags',  'image'
        )
        widgets = {
            'body': forms.Textarea(attrs={
                'rows': 4,
                'class': "w-full bg-bgDark border border-borderDark rounded-md px-3 py-2 text-sm resize-none focus:outline-none focus:border-primary",
                # 'placeholder': ''
            }),
            'code': forms.Textarea(attrs={
                'rows':6,
                'class': "w-full bg-bgDark border border-borderDark rounded-md px-3 py-2 text-sm font-mono resize-none focus:outline-none focus:border-primary",
                'placeholder': "Kodingizni qoldiring"
            }),
            'image': forms.ClearableFileInput(attrs={
                "class": "block w-full text-sm text-textMuted file:mr-4 file:py-2 file:px-4 file:rounded-md file:border-0 file:bg-gray-800 file:text-white hover:file:bg-gray-700"
            }),
        }