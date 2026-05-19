from django import forms

from .models import Blog


class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ["title", "content", "photo", "publication_sing"]
        labels = {
            "title": "Заголовок",
            "content": "Содержимое",
            "photo": "Фотография",
            "publication_sing": "Признак публикации",
        }
        widgets = {
            "content": forms.Textarea(
                attrs={"rows": 10, "placeholder": "Введите текст публикации..."}
            ),
            "title": forms.TextInput(attrs={"placeholder": "Введите заголовок поста"}),
        }
