from django import forms

from .models import Fb


class FbForm(forms.ModelForm):
    # captcha = CaptchaField(label='Введите текст с картинки', error_messages={'invalid': 'Неправильный текст'})
    name = forms.CharField(min_length=2,max_length=30,required=True, label='Имя')
    phone = forms.CharField(min_length=10,required=True, max_length=20, help_text='Ввод номера в формате +7 999 999 99 99')

    class Meta:
        model = Fb
        fields = ('name', 'phone')
