from django.conf.urls import * #patterns, include, url
from django.template import Context, loader

#from django.views.generic.simple import direct_to_template

urlpatterns = patterns('',
    #url(r'^', 'base' ),#name='wb_landingpage'),
    url(r'^$', 'gameplay.views.base' ,name='wb_landingpage'),
    url(r'^StartGame/Location/$','gameplay.views.choose_location',name='location'),
    url(r'^StartGame/SetupRoster/$','gameplay.views.fill_roster',name='roster'),
    url(r'^Play/$','gameplay.views.gameplay',name='play_ball'),
    url(r'^Contribute/','gameplay.views.contribute',name='contribute'),
    url(r'^Roster/','gameplay.views.player_stats',name='player_stats'),
    url(r'^GameHistory/','gameplay.views.game_history',name='game_history'),
    
)

'''
from django.conf import settings
from django.conf.urls.static import static
if settings.DEBUG:
    urlpatterns += patterns('',
        (r'^%s/(?P<path>.*)$' % settings.STATIC_URL[1:-1],
        'django.views.static.serve',
        {'document_root':  settings.STATIC_ROOT, 'show_indexes': False}),
    )
'''
