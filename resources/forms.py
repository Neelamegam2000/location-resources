from django import forms

from resources.models import resources


class resourcesForm(forms.ModelForm):
    class Meta:
        model = resources
        fields = ('name','location','pincode','work','address','phone_number','email')

