from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from .models import task
from .forms import TodoForms
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView, DeleteView


class Tasklist(ListView):
    model = task
    template_name = 'home.html'
    context_object_name = 'task12'


class Taskdetail(DetailView):
    model = task
    template_name = 'detail.html'
    context_object_name = 'task1'


class Taskupdate(UpdateView):
    model = task
    template_name = 'update.html'
    context_object_name = 'task1'
    fields = ('name', 'priority', 'date')

    def get_success_url(self):
        return reverse_lazy('cbvdetail', kwargs={'pk': self.object.id})


class Taskdelete(DetailView):
    model = task
    template_name = 'delete.html'
    success_url = reverse_lazy('cbvhome')


# Create your views here.
def home(request):
    task12 = task.objects.all()
    if request.method == 'POST':
        name = request.POST.get('task', '')
        priority = request.POST.get('priority', '')
        date = request.POST.get('date', ' ')
        task1 = task(name=name, priority=priority, date=date)
        task1.save()
    return render(request, 'home.html', {'task12': task12})


# def detail(request):

# return render(request, 'detail.html', )

def delete(request, id):
    task13 = task.objects.get(id=id)
    if request.method == 'POST':
        task13.delete()
        return redirect('/')

    return render(request, 'delete.html')


def update(request, id):
    task1 = task.objects.get(id=id)
    f = TodoForms(request.POST or None, instance=task1)
    if f.is_valid():
        f.save()
        return redirect('/')
    return render(request, 'edit.html', {'f': f, 'task1': task1})
