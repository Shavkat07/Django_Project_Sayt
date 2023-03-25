from .models import Articles
from django.forms import ModelForm, TextInput, DateTimeInput, Textarea


class ArticlesForm(ModelForm):
    class Meta:
        model = Articles
        fields = ['title', 'anons', 'full_text', 'date']
        widgets = {
            'title': TextInput(attrs={
                "class": "form-control",
                "placeholder": "Maqola Nomi"

            }),
            'anons': TextInput(attrs={
                "class": "form-control",
                "placeholder": "Maqola Anonsi"
            }),
            'date': DateTimeInput(attrs={
                "class": "form-control",
                "placeholder": "Chiqarilgan Sana"
            }),
            'full_text': Textarea(attrs={
                "class": "form-control",
                "placeholder": "Maqola Matni"
            })
        }