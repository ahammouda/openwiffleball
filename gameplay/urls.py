from django.conf.urls import * #patterns, include, url
from django.template import Context, loader

#from django.views.generic.simple import direct_to_template

urlpatterns = patterns('',
    url(r'^$', 'gameplay.views.base' ,name='wb_landingpage'),
    url(r'^StartGame/Location/$','gameplay.views.choose_location',name='location'),
    url(r'^StartGame/SetupRoster/$','gameplay.views.fill_roster',name='roster'),
    url(r'^StartGame/OrderPlayers/$','gameplay.views.order_play',name='player_order'),

    url(r'^Play/$','gameplay.views.gameplay',name='play_ball'),
    url(r'^Contribute/','gameplay.views.contribute',name='contribute'),
    url(r'^Roster/','gameplay.views.player_stats',name='player_stats'),
    url(r'^GameHistory/','gameplay.views.game_history',name='game_history'),
)
