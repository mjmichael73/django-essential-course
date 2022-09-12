from .forms import NotesForm
from .models import Notes
from django.views.generic import ListView, DetailView, CreateView, UpdateView


class NotesCreateView(CreateView):
    model = Notes
    success_url = "/smart/notes/"
    form_class = NotesForm


class NotesUpdateView(UpdateView):
    model = Notes
    success_url = "/smart/notes/"
    form_class = NotesForm


class NotesListView(ListView):
    model = Notes
    context_object_name = "notes"
    template_name = "notes/notes_list.html"


class NotesDetailView(DetailView):
    model = Notes
    context_object_name = "note"
    template_name = "notes/notes_detail.html"
