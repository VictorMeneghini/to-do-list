from django.shortcuts import redirect, render, get_object_or_404
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView

from .models import Status
from .forms import StatusForm


class CreateStatus(CreateView):
    template_name = 'status/form.html'
    model = Status
    fields = ['name', 'order']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = StatusForm()
        return context

    def post(self, request, *args, **kwargs):
        form = StatusForm(request.POST)

        if form.is_valid():
            board_id = kwargs['pk']
            form.save(board_id)
            return redirect(reverse("board:board_home", args=(kwargs['pk'],)))
        else:
            context = self.get_context_data()
            context["form"] = form
            return render(request, self.template_name, context)


class UpdateStatus(UpdateView):
    model = Status
    fields = ['name', 'order']
    template_name = 'status/form.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        status = get_object_or_404(Status, pk=self.kwargs["pk"])
        data = {
            "name": status.name,
            "order": status.order,
        }

        context["form"] = StatusForm(data=data)
        return context

    def post(self, request, *args, **kwargs):
        status = get_object_or_404(Status, pk=self.kwargs["pk"])
        form = StatusForm(request.POST, request.FILES, instance=status)

        if form.is_valid():
            form.save(status.board_id)
            return redirect(reverse("board:board_home", args=(status.board_id,)))
        else:
            context = self.get_context_data()
            context["form"] = form
            return render(request, self.template_name, context)


class StatusDelete(DeleteView):
    model = Status

    def get_success_url(self, **kwargs):
        board_id = self.object.board.id
        return reverse_lazy('board:board_home', args=(board_id,))
