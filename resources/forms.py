from secrets import choice
from django import forms

from resources.models import resources, status

statusdata=(("Available","Available"),("On Duty","On Duty"),("Break","Break"),("Open","Open"),("closed","Closed"))
class resourcesForm(forms.ModelForm):
    class Meta:
        model = resources
        fields = ('name','location','pincode','work','address','phone_number','email','profile_picture')
class statusForm(forms.ModelForm):
    class Meta:
        model = status
        fields = ('status',)