from django import forms
from django.core.exceptions import ValidationError

from .models import *


class AddPostForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['cat'].empty_label = "Категорія не вибрана"

    class Meta:
        model = Women
        fields = '__all__'
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-input'}),
            'content': forms.Textarea(attrs={'cols': 60, 'row': 10})
        }

    def clean_title(self):
        title = self.cleaned_data['title']
        if len(title) > 200:
            raise ValidationError('Завелика довжина')
        return title

    # title = forms.CharField(max_length=255, label="Заголовок", widget=forms.TextInput(attrs={'class': 'form-input'}))
    # slug = forms.SlugField(max_length=255, label="URL")
    # content = forms.CharField(widget=forms.Textarea(attrs={'cols': 60, 'row': 10}), label="Контент")
    # is_published = forms.BooleanField(label="Опублікувати", required=False, initial=True)
    # cat = forms.ModelChoiceField(queryset=Category.objects.all(), label="Категорії", empty_label="Категорія не вибрана")
