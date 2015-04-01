from django.db import models


class RankingUpdate(models.Model):
    instant = models.DateTimeField(auto_now_add=True)

    class Meta:
        app_label = 'crawler'
