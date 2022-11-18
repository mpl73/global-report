from django.views.generic import TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from . import models  
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin


# class CartaoCreate(CreateView):
#     model = models.Cartao
#     form_class = forms.CartaoForm
#     template_name = 'cartoes/form.html'
#     success_url = reverse_lazy('cartoes')

# class CartaoUpdate(UpdateView):
#     model = models.Cartao
#     form_class = forms.CartaoForm
#     template_name = 'cartoes/form.html'
#     success_url = reverse_lazy('cartoes')

# class CartaoDelete(DeleteView):
#     model = models.Cartao
#     template_name = 'cartoes/form_excluir.html'
#     success_url = reverse_lazy('cartoes')

# class CartaoList(ListView):
#     model = models.Cartao
#     template_name = 'cartoes/cartoes.html'

class MonitoramentoKPIsView(LoginRequiredMixin, TemplateView):
    template_name = 'monitoramento_kpis/monitoramento_kpis.html'

class VariaveisVirtuaisView(LoginRequiredMixin, TemplateView):
    template_name = 'monitoramento_kpis/variaveis_virtuais.html'