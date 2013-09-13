
from django import forms
from gameplay.models import Player
#from django.forms.widgets import CheckboxSelectMultiple

class LocationForm(forms.Form):
    location=forms.CharField(max_length=255)
    
class ExistingPlayerForm(forms.Form):
    existing=forms.ModelMultipleChoiceField(queryset=Player.objects.all(),
                                            widget=forms.CheckboxSelectMultiple() )

class NewPlayerForm(forms.Form):
    new=forms.CharField(max_length=255)

class PlayerCountForm(forms.Form):
    count=forms.IntegerField(min_value=0)
