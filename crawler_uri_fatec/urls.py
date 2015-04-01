from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include('ranking.urls')),
    url(r'^atualizar_rankings/?$', 'crawler.views.atualizar_rankings', name='atualizar-rankings')
)
