from django.shortcuts import redirect, render, get_object_or_404
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView

from .models import Task
from .forms import TaskForm


class CreateTask(CreateView):
    template_name = 'task/form.html'
    model = Task
    fields = ['name', 'description']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = TaskForm()
        return context

    def post(self, request, *args, **kwargs):
        form = TaskForm(request.POST)
        if form.is_valid():
            status_id = kwargs['pk']
            form.save(status_id)
            return redirect(reverse("board:index"))
        else:
            context = self.get_context_data()
            context["form"] = form
            return render(request, self.template_name, context)


class UpdateTask(UpdateView):
    model = Task
    fields = ['name', 'description']
    template_name = 'status/form.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        task = get_object_or_404(Task, pk=self.kwargs["pk"])
        data = {
            "name": task.name,
            "description": task.description,
        }

        context["form"] = TaskForm(data=data)
        return context

    def post(self, request, *args, **kwargs):
        task = get_object_or_404(Task, pk=self.kwargs["pk"])
        form = TaskForm(request.POST, request.FILES, instance=task)

        if form.is_valid():
            form.save(task.status_id)
            return redirect(reverse("board:index"))
        else:
            context = self.get_context_data()
            context["form"] = form
            return render(request, self.template_name, context)


class TaskDelete(DeleteView):
    model = Task
    success_url = reverse_lazy('board:index')

