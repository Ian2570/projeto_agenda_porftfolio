from django import forms
from django.core.exceptions import ValidationError
from . import models


class ContactForm(forms.ModelForm):
    class Meta:
        model = models.Contact
        fields = ( 'first_name', 'last_name', 'phone', 'email', 'description', 'category', 'picture',)

    def clean(self):
        #cleaned_data = self.cleaned_data

        #self.add_error( 'first_name', ValidationError('Mensagem de erro', code='invalid'))
        return super().clean()
    
    def clean_first_name(self):
        first_name = self.cleaned_data.get('first_name')

        if first_name == 'ABC':
            raise ValidationError(
                'Não difite ABC neste campo',
                code='invalid'
            )
        return first_name