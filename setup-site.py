from django.core.management import setup_environ
from wiffleball import settings

setup_environ(settings)

# This is necessary for the auto-generated emails that 
# go out when people register.  The site.name/etc won't be
# correct without this setup, and I'm too lazy to hack up
# my own templates for that stuff.
from django.contrib.sites.models import Site
s=Site(domain='openwiffleball.com',name='Openwiffleball')
s.save()
print s.pk #Guaranteed to be 2 for all circumstances I can think of, but never know
