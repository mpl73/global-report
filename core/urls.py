# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.contrib import admin
from django.urls import path, include  # add this

urlpatterns = [
    path('admin/', admin.site.urls),          # Django admin route
    path("", include("apps.authentication.urls")), # Auth routes - login / register

    # ADD NEW Routes HERE

    # Leave `Home.Urls` as last the last line
    path("", include("apps.home.urls")),
    path("tabela_monitoramento/", include("apps.tabela_monitoramento.urls")),
    path("grafico_tendencias/", include("apps.grafico_tendencias.urls")),
    path("variaveis_estaticas/", include("apps.variaveis_estaticas.urls")),
    path("monitoramento_kpis/", include("apps.monitoramento_kpis.urls")),
]
