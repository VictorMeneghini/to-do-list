from django.shortcuts import redirect, render, get_object_or_404
from django.urls import reverse, reverse_lazy
from django.views.generic import TemplateView, CreateView, DeleteView, UpdateView

from .models import Board
from .forms import BoardForm


class Index(TemplateView):
    template_name = 'board/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        print(self.request.user.id)
        context['all_boards'] = Board.objects.filter(owner=self.request.user)
        return context


class CreateBoard(CreateView):
    template_name = 'board/form.html'
    model = Board
    fields = ['name', 'description']
    success_url = reverse_lazy("board:index")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = BoardForm()
        return context

    def form_valid(self, form):
        result = super().form_valid(form)
        form.instance.owner.add(self.request.user)
        return result

class BoardUpdate(UpdateView):
    model = Board
    fields = ['name', 'description']
    template_name = 'board/form.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        board = get_object_or_404(Board, pk=self.kwargs["pk"])
        data = {
            "name": board.name,
            "description": board.description,
        }

        context["form"] = BoardForm(data=data)
        return context

    def post(self, request, *args, **kwargs):
        board = get_object_or_404(Board, pk=self.kwargs["pk"])
        form = BoardForm(request.POST, request.FILES, instance=board)

        if form.is_valid():
            form.save(self.request)
            return redirect(reverse("board:index"))
        else:
            context = self.get_context_data()
            context["form"] = form
            return render(request, self.template_name, context)


class BoardDelete(DeleteView):
    model = Board
    success_url = reverse_lazy('board:index')


def board_home(request, *args, **kwargs):
    context = {}
    current_board = get_object_or_404(Board, pk=kwargs['pk'])
    context['current_board'] = current_board
    context['columns'] = current_board.status.all()
    return render(request, 'board/board.html', context)
