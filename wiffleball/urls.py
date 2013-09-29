from django.conf.urls import patterns, include, url
#from django.views.generic.simple import direct_to_template

#from registration.backends.default.urls import *

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()
import os

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'wiffleball.views.home', name='home'),
    # url(r'^admin/', include('django.contrib.admin.urls')),
    url(r'^', include('gameplay.urls')),
    url(r'^accounts/', include('registration.backends.default.urls') ),
    url(r'^accounts/profile/$','gameplay.views.home',name='home'),
    
    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    
    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)

from django.contrib.auth import views as auth_views

urlpatterns += patterns('',
                       url(r'^login/$',
                           auth_views.login,
                           {'template_name': 'registration/login.html'},
                           name='auth_login'),
                       url(r'^logout/$',
                           auth_views.logout,
                           {'template_name':'registration/logout.html'},
                           name='auth_logout'),
                       url(r'^logout/$',
                           auth_views.logout,
                           {'template_name': 'registration/logout.html'},
                           name='auth_logout'),
                       url(r'^password/change/$',
                           auth_views.password_change,
                           name='auth_password_change'),
                       url(r'^password/change/done/$',
                           auth_views.password_change_done,
                           name='auth_password_change_done'),
                       url(r'^password/reset/$',
                           auth_views.password_reset,
                           name='auth_password_reset'),
                       url(r'^password/reset/confirm/(?P<uidb36>[0-9A-Za-z]+)-(?P<token>.+)/$',
                           auth_views.password_reset_confirm,
                           name='auth_password_reset_confirm'),
                       url(r'^password/reset/complete/$',
                           auth_views.password_reset_complete,
                           name='auth_password_reset_complete'),
                       url(r'^password/reset/done/$',
                           auth_views.password_reset_done,
                           name='auth_password_reset_done'),
)

if os.environ['LOCAL_MACHINE']=='true':
    from django.conf import settings
    from django.conf.urls.static import static
    if settings.DEBUG:
        urlpatterns += patterns('',
            (r'^%s/(?P<path>.*)$' % settings.STATIC_URL[1:-1],
            'django.views.static.serve',
            {'document_root':  settings.STATIC_ROOT, 'show_indexes': False}),
    )
