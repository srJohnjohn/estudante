from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from .models import Aluno

# Create your views here.

class AlunoList(generic.ListView):
    model = Aluno
    paginate_by = 25

class AlunoCreate(CreateView):
    model = Aluno
    fields = ['nome', 'nacimento', 'status']

class AlunoDetailView(generic.DetailView):
    model = Aluno

class AlunoUpdate(UpdateView):
    model = Aluno
    fields = '__all__'
    template_name_suffix = '_update_form'

class AlunoDelete(DeleteView):
    model = Aluno
    success_url = reverse_lazy('aluno_list')
