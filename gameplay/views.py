# Create your views here.
from models import Player, Game
import string

from django import forms
from datetime import datetime
from forms import LocationForm, ExistingPlayerForm, NewPlayerForm, PlayerCountForm
from utils import add_player
from django.forms.formsets import formset_factory

from django.template import Context, loader, RequestContext
from django.http import HttpResponse
from django.shortcuts import render_to_response, redirect

from django.contrib.auth.decorators import login_required

def base(request):
    template = loader.get_template('gameplay/landing_wball.html')
    if request.user.is_authenticated():
        context = RequestContext(request, {'logged_in': True})
        return HttpResponse(template.render(context))
    else:
        context = RequestContext(request, {'logged_in': False})
        return HttpResponse(template.render(context))

def contribute(request):
    template = loader.get_template('gameplay/contribute_wball.html')
    if request.user.is_authenticated():
        context = RequestContext(request, {'logged_in': True })
        return HttpResponse(template.render(context))
    else:
        context = RequestContext(request, {'logged_in': False})
        return HttpResponse(template.render(context))

@login_required
def home(request):
    template = loader.get_template('gameplay/home_wball.html')
    context = RequestContext(request,{'logged_in': True})
    return HttpResponse(template.render(context))

@login_required
def choose_location(request):
    LocationFormSet=formset_factory(LocationForm)
    if request.method=='POST':
        location_formset=LocationFormSet(request.POST, request.FILES, prefix='location')
        if location_formset.is_valid():
            for form in location_formset:
                print form.cleaned_data['location']
                print datetime.now()
                g=Game(location=form.cleaned_data['location'],date=datetime.now(),\
                           user=request.user)
                g.save()
            return redirect('gameplay.views.fill_roster')
        else:
            print 'Location ERRORS: '+location_formset.errors
    else:
        # TODO: Save locations separately and
        # check to see if they exist
        location_formset=LocationFormSet(prefix='location')
        context = RequestContext(request,{'title': 'Setup Game: Location',
                                          'location_formset': location_formset,
                                          'logged_in': True})
        return render_to_response('gameplay/choose_location.html',context)

@login_required
def fill_roster(request):
    """
    Write Now sort of hacky logic which takes you through filling out 
    a roster for a particular game.  Eventually would like to have
    all of this on a single dynamic form, rather than a number of separate
    forms.
    """
    PlayerCountFormSet=formset_factory(PlayerCountForm)
    ExistPlayerFormSet=formset_factory(ExistingPlayerForm)
    NewPlayerFormSet=formset_factory(NewPlayerForm)
    if request.method=='POST':
        num_players=0
        if 'player_count-INITIAL_FORMS' in request.REQUEST.keys():
            count_fs=PlayerCountFormSet(request.POST,request.FILES,prefix='player_count')
            if count_fs.is_valid():
                for form in count_fs:
                    num_players=form.cleaned_data['count']
        
        if 'exist_players-INITIAL_FORMS' in request.REQUEST.keys():
            exist_player_fs=ExistPlayerFormSet(request.POST,request.FILES,\
                                                   prefix='exist_players')
            if exist_player_fs.is_valid():
                game=Game.objects.filter(user=request.user).latest('date')
                for form in exist_player_fs:
                    players=form.cleaned_data['existing']
                    for player in players:
                        pqs=Player.objects.filter(name=player)
                        for p in pqs:
                            p.games.add(game)
        
        elif 'new_players-INITIAL_FORMS' in request.REQUEST.keys():
            new_player_fs=NewPlayerFormSet(request.POST,request.FILES,\
                                               prefix='new_players')
            if new_player_fs.is_valid():
                game=Game.objects.filter(user=request.user).latest('date')
                count=0
                err_players=list()
                for form in new_player_fs:
                    new_guy=form.cleaned_data['new']
                    if Player.objects.filter(name=new_guy,user=request.user).exists():
                        err_players.append(form.cleaned_data['new'])
                    else:
                        p=Player(name=new_guy,user=request.user)
                        p.save()
                        p.games.add(game)
                    count+=1
                n_redundant=len(err_players)
                if n_redundant>0:
                    NewPlayerFormSet=formset_factory(NewPlayerForm,extra=count)
                    message=""
                    if n_redundant>1:
                        print err_players[0]
                        message=[string.join([str(message),str(player),", "]) for player in err_players]
                        
                        message=string.join([str(message),"are"]," ")
                    else: message=message+err_players[0]+" is"
                    message=message+" already on your roster."\
                        "  You can only add new players in this step."
                    return add_player(request,NewPlayerFormSet,message)
                else:
                    return redirect('gameplay.views.gameplay')
        
        if num_players==0:
            return redirect('gameplay.views.gameplay')
        else:
            NewPlayerFormSet=formset_factory(NewPlayerForm,extra=num_players)
            return add_player(request,NewPlayerFormSet,None)
    else:
        "******************  Non-POST Request *********************"
        count_formset=PlayerCountFormSet(prefix='player_count')
        if Player.objects.filter(user=request.user).count()>=1:
            exist_player_fs=ExistPlayerFormSet(prefix='exist_players')
            template = loader.get_template('gameplay/choose_players.html')
            context = RequestContext(request, {'title': 'Setup Game: Build Roster',
                                               'count_formset': count_formset ,
                                               'exist_player_fs': exist_player_fs,
                                               'logged_in': True})
        else:
            template = loader.get_template('gameplay/how_many.html')
            context = RequestContext(request, {'title': 'Setup Game: Build Roster',
                                               'count_formset': count_formset,
                                               'logged_in': True})
        return HttpResponse(template.render(context))

@login_required
def player_stats(request):
    """
    List Player attributes that are editable (right now just name).
    as well as there computed stats on Ks and Os etc (uneditable).
    """
    players=Player.objects.filter(user=request.user)
    template = loader.get_template('gameplay/player_stats_wball.html')
    context = RequestContext(request,{'title':'Your Roster',
                                      'players':players,
                                      'logged_in': True})
    return HttpResponse(template.render(context))

@login_required
def game_history(request):
    """
    List Every game.  Order by date (most recent to oldest)
    """
    games=Game.objects.filter(user=request.user)
    template = loader.get_template('gameplay/game_stats_wball.html')
    context = RequestContext(request,{'title':'Your Roster',
                                      'games':games,
                                      'logged_in': True})
    return HttpResponse(template.render(context))
    
@login_required
def gameplay(request):
    """
    Meet of the app should go here.  We want to make the 
    play_wball.html very easily updated with ajax, etc.
    """
    g=Game.objects.filter(user=request.user).latest('date')
    today=g.date
    location=g.location
    players=Player.objects.filter(games=g.pk)
    
    template = loader.get_template('gameplay/play_wball.html')
    context = RequestContext(request,{'title':'Play Ball!','today':today,
                                      'location':location,'players':players,
                                      'logged_in': True})
    return HttpResponse(template.render(context))

