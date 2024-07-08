from django import forms
from mailing.models import Client, MailingText


class StyleFormMixin:

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if isinstance(field, forms.BooleanField):
                field.widget.attrs['class'] = "form-check-input"
            else:
                field.widget.attrs['class'] = "form-control"


class ClientForm(StyleFormMixin, forms.ModelForm):

    class Meta:
        model = Client
        exclude = ('owner',)


class MailingTextForm(StyleFormMixin, forms.ModelForm):

    class Meta:
        model = MailingText
        exclude = ('owner',)
