from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView

from to_do_list.board.models import Board
from .models import Status
from .forms import StatusForm


class CreateStatus(CreateView):
    template_name = 'status/form.html'
    model = Status
    form_class = StatusForm

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['board'] = get_object_or_404(Board, pk=self.kwargs.get('pk'))
        return kwargs

    def get_success_url(self, **kwargs):
        board_pk = self.object.board.pk
        return reverse_lazy('board:board_home', args=(board_pk,))


class UpdateStatus(UpdateView):
    model = Status
    template_name = 'status/form.html'
    form_class = StatusForm

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['board'] = get_object_or_404(Board, pk=self.kwargs.get('pk'))
        return kwargs

    def get_success_url(self, **kwargs):
        board_pk = self.object.board.pk
        return reverse_lazy('board:board_home', args=(board_pk,))


class StatusDelete(DeleteView):
    model = Status

    def get_success_url(self, **kwargs):
        board_id = self.object.board.id
        return reverse_lazy('board:board_home', args=(board_id,))
