from django import template
from testpyproject.python_game.models import PythonGameResult
from django.shortcuts import loader
register = template.Library()

@register.simple_tag
def best_gamers():
    gamers = PythonGameResult.objects.order_by('score').reverse().all()[:3]
    return loader.render_to_string("python_game/best_gamers.html", {'gamers': gamers})