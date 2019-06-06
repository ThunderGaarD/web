from django import forms
from django.core.exceptions import ValidationError
from django.forms import TextInput, EmailInput
from workshop.subscriptions.models import Subscriptions

from workshop.subscriptions.validators import validate_cpf


# class SubscriptionForm(forms.Form):
#
#     name = forms.CharField(label='Nome',
#                            widget=forms.TextInput(attrs={'class': 'contact_input',
#                                                          'placeholder': 'Nome'}))
#     cpf = forms.CharField(label='CPF',validators=[validate_cpf],
#                           widget=forms.TextInput(attrs={'class':'contact_input',
#                                                         'placeholder':'CPF'}))
#     email = forms.EmailField(label='Email',
#                              widget=forms.EmailInput(attrs={'class':'contact_input',
#                                                             'placeholder':'Email'}), required=False)
#     phone = forms.CharField(label='Telefone',
#                             widget=forms.TextInput(attrs={'class':'contact_input',
#                                                           'placeholder':'Telefone'}), required=False)
#
#     def clean_name(self):
#
#         name = self.cleaned_data['name']
#         words = [w.capitalize() for w in name.split()]
#
#         return ' '.join(words)
#
#
#     def clean(self):
#
#         if not self.cleaned_data.get('email') and not self.cleaned_data.get('phone'):
#             raise ValidationError('Informe seu Email ou Telefone')
#
#         return self.cleaned_data


class SubscriptionForm(forms.ModelForm):

    class Meta:

        model = Subscriptions
        fields = ['name', 'cpf', 'email', 'phone']
        widgets= {'name':TextInput(attrs={'class': 'contact_input', 'placeholder': 'Nome'}),
                  'cpf':TextInput(attrs={'class': 'contact_input', 'placeholder': 'CPF'}),
                  'email':EmailInput(attrs={'class': 'contact_input', 'placeholder': 'E-Mail'}),
                  'phone':TextInput(attrs={'class': 'contact_input', 'placeholder': 'Telefone'})}


    def clean_name(self):

        name = self.cleaned_data['name']
        words = [w.capitalize() for w in name.split()]

        return ' '.join(words)


    def clean(self):

        if not self.cleaned_data.get('email') and not self.cleaned_data.get('phone'):
            raise ValidationError('Informe seu Email ou Telefone')

        return self.cleaned_data
