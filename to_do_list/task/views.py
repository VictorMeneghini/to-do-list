from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView

from to_do_list.status.models import Status
from .models import Task
from .forms import TaskForm


class CreateTask(CreateView):
    template_name = 'task/form.html'
    model = Task
    form_class = TaskForm

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['status'] = get_object_or_404(Status, pk=self.kwargs.get('pk'))
        return kwargs

    def get_success_url(self, **kwargs):
        board_pk = self.object.status.board.pk
        return reverse_lazy('board:board_home', args=(board_pk,))


class UpdateTask(UpdateView):
    template_name = 'task/form.html'
    model = Task
    form_class = TaskForm

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['status'] = get_object_or_404(Status, pk=self.kwargs.get('pk'))
        return kwargs

    def get_success_url(self, **kwargs):
        board_pk = self.object.status.board.pk
        return reverse_lazy('board:board_home', args=(board_pk,))


class TaskDelete(DeleteView):
    model = Task
    success_url = reverse_lazy('board:index')
