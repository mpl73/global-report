from django.views.generic import TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
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

class AlarmesView(LoginRequiredMixin, TemplateView):
    template_name = 'alarmes/alarmes.html'

    def get_context_data(self, **kwargs):
        context = super(AlarmesView, self).get_context_data(**kwargs)
        context['title'] = 'Alarmes'
        context['list'] = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
        return context