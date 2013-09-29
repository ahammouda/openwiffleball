from gameplay.models import Game, Player, Inning, BatterScore, PitcherScore
from django.contrib import admin

admin.site.register(Game)
admin.site.register(Player)
admin.site.register(Inning)
admin.site.register(BatterScore)
admin.site.register(PitcherScore)
