from django import forms
from .models import Post


class PostCreateForm(forms.ModelForm):
    """
    Форма добавления статей на сайте
    """

    class Meta:
        model = Post
        fields = ('title', 'category', 'description', 'text', 'thumbnail', 'status')

    def __init__(self, *args, **kwargs):
        """
        Обновление стилей формы под Bootstrap
        """
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({
                'class': 'form-control',
                'autocomplete': 'off'
            })


class PostUpdateForm(PostCreateForm):
    """
    Форма обновления статьи на сайте
    """

    class Meta:
        model = Post
        fields = PostCreateForm.Meta.fields + ('updater', 'fixed')

    def __init__(self, *args, **kwargs):
        """
        Обновление стилей формы под Bootstrap
        """
        super().__init__(*args, **kwargs)

        self.fields['fixed'].widget.attrs.update({
            'class': 'form-check-input'
        })

