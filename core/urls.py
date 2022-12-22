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
    path("historico_alarmes/", include("apps.historico_alarmes.urls")),
    path("relatorios/", include("apps.relatorios.urls")),
    path("dashboards/", include("apps.dashboards.urls")),
    path("monitoramento_kpis/", include("apps.monitoramento_kpis.urls")),
    path("tarefas/", include("apps.tarefas.urls")),
    path("variaveis_estaticas/", include("apps.variaveis_estaticas.urls")),

    path("coletores/", include("apps.coletores.urls")),
    path("unidades/", include("apps.unidades.urls")),
    path("usuarios/", include("apps.usuarios.urls")),

    path("driver_opc/", include("apps.driver_opc.urls")),
    path("driver_siemens/", include("apps.driver_siemens.urls")),
    path("variaveis_monitoradas/", include("apps.variaveis_monitoradas.urls")),
    path("alarmes/", include("apps.alarmes.urls")),
]
