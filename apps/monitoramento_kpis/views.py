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

    def get_context_data(self, **kwargs):
        context = super(MonitoramentoKPIsView, self).get_context_data(**kwargs)
        context['title'] = "Monitoramento de KPI's"
        context['list'] = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
        return context

class VariaveisVirtuaisView(LoginRequiredMixin, TemplateView):
    template_name = 'monitoramento_kpis/variaveis_virtuais.html'

    def get_context_data(self, **kwargs):
        context = super(VariaveisVirtuaisView, self).get_context_data(**kwargs)
        context['title1'] = "Monitoramento de KPI's"
        context['title2'] = "Variavéis Virtuais"
        context['list'] = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
        return context