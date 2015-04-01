# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('participantes', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='pontuacao',
            options={'verbose_name': 'pontua\xe7\xe3o', 'verbose_name_plural': 'pontua\xe7\xf5es'},
        ),
        migrations.AlterField(
            model_name='pontuacao',
            name='participante',
            field=models.ForeignKey(related_name='pontuacoes', to='participantes.Participante'),
            preserve_default=True,
        ),
    ]
