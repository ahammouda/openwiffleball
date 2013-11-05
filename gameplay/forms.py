
from django import forms
from django.forms.models import BaseModelFormSet
from gameplay.models import Player
#from django.forms.widgets import CheckboxSelectMultiple

class LocationForm(forms.Form):
    location=forms.CharField(max_length=255)
    
class ExistingPlayerForm(forms.Form):
    existing=forms.ModelMultipleChoiceField(widget=forms.CheckboxSelectMultiple(),
                                            queryset=Player.objects.none()
                                            )
    def __init__(self, *args, **kwargs):
        user_filter=kwargs.pop('user_filter')
        super(ExistingPlayerForm, self).__init__(*args, **kwargs)
        self.fields['existing'].queryset=Player.objects.filter(user=user_filter)
        
class NewPlayerForm(forms.Form):
    new=forms.CharField(max_length=255)

class PlayerCountForm(forms.Form):
    count=forms.IntegerField(min_value=0)

class PitcherOrderForm(forms.ModelForm):
    position=forms.IntegerField(min_value=0,required=False)
    pitchers=forms.ModelChoiceField(queryset=Player.objects.none(),
                                    empty_label="Choose Pitcher",
                                    required=False)
    class Meta:
        model=Player
        exclude=('id',
                 'games',
                 'user',
                 'name')

class PitcherOrderFormSet(BaseModelFormSet):
    def __init__(self, *args, **kwargs):
        super(PitcherOrderFormSet, self).__init__(*args, **kwargs)
        for index,form in enumerate(self.forms):
            form.fields['pitchers'].queryset=self.queryset

class BatterOrderForm(forms.ModelForm):
    position=forms.IntegerField(min_value=0,required=False)
    batters=forms.ModelChoiceField(queryset=Player.objects.none(),
                                   empty_label="Choose Batter",
                                   required=True)
    class Meta:
        model=Player
        exclude=('id',
                 'games',
                 'user',
                 'name')
        
class BatterOrderFormSet(BaseModelFormSet):
    def __init__(self, *args, **kwargs):
        super(BatterOrderFormSet, self).__init__(*args, **kwargs)
        for index,form in enumerate(self.forms):
            form.fields['batters'].queryset=self.queryset

#widgets={
#    'pitchers':forms.ChoiceField(choices=choices)
#    }
        
#def __init__(self, *args, **kwargs):
#    super(PitcherOrderForm, self).__init__(*args, **kwargs)
#    self.fields['name'].label = 'pitchers'
        
            
#widgets={
#    'name':forms.ChoiceField(choices=choices)
#    }
    #def __init__(self, *args, **kwargs):
    #    super(BatterOrderForm, self).__init__(*args, **kwargs)
    #    #self.fields['name'].widget = forms.SelectField(choices=cur_choices)
    #    #self.fields['name'].label = 'batters'
        
    #def update_widget(self. *args, **kwargs):
