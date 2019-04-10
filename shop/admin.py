from django.contrib import admin
from .models import Developer, Player, Game

# Register your models here.

admin.site.register(Developer)
admin.site.register(Player)
admin.site.register(Game)
