from django.urls import path
from . import views

urlpatterns = [
    path('', views.MonitoramentoKPIsView.as_view(), name='monitoramento_kpis'),
    path('variaveis_virtuais/', views.VariaveisVirtuaisView.as_view(), name='variaveis_virtuais'),
    # path('cartoes/', views.CartaoList.as_view(), name='cartoes'),
    # path('novo/cartao', views.CartaoCreate.as_view(), name='novo_cartao'),
    # path('editar/cartao/<int:pk>', views.CartaoUpdate.as_view(), name='editar_cartao'),
    # path('excluir/cartao/<int:pk>', views.CartaoDelete.as_view(), name='excluir_cartao'),
]