from django import forms
from .choices import *

class ReliantPartyForm(forms.Form):   
    id = forms.CharField(max_length=255, widget=forms.HiddenInput(), required = False)
    name = forms.CharField(max_length=255)
    status = forms.ChoiceField(choices = STATUS_CHOICES, initial="New", widget=forms.Select())
    email = forms.EmailField(max_length=255)
    abn = forms.CharField(max_length=255)
    address_street_1 = forms.CharField(max_length=255)
    address_street_2 = forms.CharField(max_length=255, required = False)
    address_state = forms.ChoiceField(choices = STATE_CHOICES, initial="ACT", widget=forms.Select())
    address_post_code = forms.IntegerField(max_value=9999)
    contact_phone = forms.CharField(max_length=255)

    def clean(self):
        cleaned_data = super(ReliantPartyForm, self).clean()
        id = cleaned_data.get('id')
        name = cleaned_data.get('name')
        email = cleaned_data.get('email')
        status = cleaned_data.get('status')
        abn = cleaned_data.get('abn')
        address_street_1 = cleaned_data.get('address_street_1')
        address_street_2 = cleaned_data.get('address_street_2')
        address_state = cleaned_data.get('address_state')
        address_post_code = cleaned_data.get('address_post_code')
        contact_phone = cleaned_data.get('contact_phone')

        if not name and not email:
            raise forms.ValidationError('Please complete name and email')

class ProviderForm(forms.Form):   
    id = forms.CharField(max_length=255, widget=forms.HiddenInput(), required = False)
    name = forms.CharField(max_length=255)
    contact = forms.CharField(max_length=255)
    businessNumber = forms.CharField(max_length=255)
    email = forms.EmailField(max_length=255)
    status = forms.ChoiceField(choices = STATUS_CHOICES, initial="New", widget=forms.Select())
    
    def clean(self):
        cleaned_data = super(ProviderForm, self).clean()
        id = cleaned_data.get('id')
        name = cleaned_data.get('name')
        email = cleaned_data.get('email')
        status = cleaned_data.get('status')
        businessNumber = cleaned_data.get('businessNumber')
        
        if not name and not email:
            raise forms.ValidationError('Please complete name and email')