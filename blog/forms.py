from django import forms
from .models import Post
from .models import Comments
from nocaptcha_recaptcha.fields import NoReCaptchaField


class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text',)


class CommentsForm(forms.ModelForm):
    captcha = NoReCaptchaField()

    class Meta:
        model = Comments
        fields = ('author', 'text')
