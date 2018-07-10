from django.contrib import admin

from .models import Game, Move
# Register your models here.

@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_player', 'second_player', 'status')
    list_editable = ('status',)

@admin.register(Move)
class MoveAdmin(admin.ModelAdmin):
    list_display = ('game', 'x', 'y')
