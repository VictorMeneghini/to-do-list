from django.shortcuts import redirect, render, get_object_or_404
from django.urls import reverse, reverse_lazy
from django.views.generic import TemplateView, CreateView, DeleteView, UpdateView

from .models import Board
from .forms import BoardForm


class Index(TemplateView):
    template_name = 'board/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['all_boards'] = Board.objects.all()
        print(context)
        return context


class CreateBoard(CreateView):
    template_name = 'board/form.html'
    model = Board
    fields = ['name', 'description']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = BoardForm()
        return context

    def post(self, request, *args, **kwargs):
        form = BoardForm(request.POST)

        if form.is_valid():
            form.save(self.request)
            return redirect(reverse("board:index"))
        else:
            context = self.get_context_data()
            context["form"] = form
            return render(request, self.template_name, context)


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
