from django.contrib.sites.models import Site
s=Site(domain='openwiffleball.com',name='Openwiffleball')
s.save()
print s.pk #Pretty much guaranteed to be 2 for most circumstances
