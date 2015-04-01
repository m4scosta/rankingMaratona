# coding: utf8

from django.conf.urls import patterns, url

urlpatterns = patterns('ranking.views',
    url('^/?$', 'ranking_paricipantes', name='ranking-paricipantes')
)
