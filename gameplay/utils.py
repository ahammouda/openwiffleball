from django import forms
from datetime import datetime
from forms import LocationForm, ExistingPlayerForm, NewPlayerForm, PlayerCountForm
from django.forms.formsets import *

from django.template import Context, loader, RequestContext
from django.http import HttpResponse
from django.shortcuts import render_to_response, redirect

def add_player(request,Formset,message):
    new_player_fs=Formset(prefix='new_players')
    template = loader.get_template('gameplay/add_players.html')
    context = RequestContext(request, {'title': 'Setup Game: Build Roster',
                                       'new_player_fs': new_player_fs,
                                       'message': message,
                                       'logged_in': True})
    return HttpResponse(template.render(context))

def start_game(request):
    '''
    if not Player.objects.all().exits():
        if request.method=='POST':
            form=PlayerCountForm(request.POST)
            
    else:
        


    if request.method=='POST':
        exist_p_formset=ExistPlayerFormSet(request.POST, request.FILES, prefix='exist_players')
        new_p_formset=NewPlayerFormSet(request.POST, request.FILES, prefix='new_players')
        
        if new_p_formset.is_valid() \
                and exist_p_formset.is_valid():
            a=1
        else:
            print 'Location ERRORS: '+location_formset.errors
            print 'Exist Player ERRORS:  '+exist_p_formset.errors
            print 'New Player ERRORS:  '+new_p_formset.errors
            raise forms.ValidationError('ManagementForm data is missing '+
                                        'or has been tampered with')
        return redirect('Play/')
    else:
        exist_p_formset=ExistPlayerFormSet(prefix='exist_players')
        new_p_formset=NewPlayerFormSet(prefix='new_players')
        context = RequestContext(request,{'title': 'Setup Game', 
                                          'location_formset': location_formset,
                                          'exist_player_fs' : exist_p_formset,
                                          'new_player_fs' : new_p_formset})
        
        return render_to_response('gameplay/startform_wball.html', context)
    '''
    pass

    
def tmp_start(request):
    LocationFormSet=formset_factory(LocationForm)

    if request.method=='POST':
        location_formset=LocationFormSet(request.POST, request.FILES, prefix='location')
        
        if location_formset.is_valid():
            a=1
        else:
            print 'Location ERRORS: '+location_formset.errors
            raise forms.ValidationError('ManagementForm data is missing '+
                                        'or has been tampered with')
        return redirect('Play/')
    else:
        location_formset=LocationFormSet(prefix='location')
        context = RequestContext(request,{'title': 'Setup Game',
                                          'location_formset': location_formset})
        return render_to_response('baseball/formset-table.html', context)
    
