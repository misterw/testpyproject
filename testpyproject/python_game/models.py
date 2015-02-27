from django.db import models
from django.db.models.manager import Manager
from django.contrib.auth.models import User
from django.utils import timezone
from django.db.models import Max

# Create your models here.

class PythonGameResultManager(Manager):
    def save_result(self, score, user):

        return self.create(
            user=user,
            score=score,
            game_date=timezone.now(),
        )

class PythonGameResult(models.Model):

    user = models.ForeignKey(User, related_name='results', null=True)
    score = models.IntegerField()
    game_date = models.DateTimeField(blank=True, null=True)

    objects = PythonGameResultManager()

