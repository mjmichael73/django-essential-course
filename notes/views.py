from .models import Notes
from django.views.generic import ListView, DetailView, CreateView


class NotesCreateView(CreateView):
    model = Notes
    fields = ['title', 'text']
    success_url = "/smart/notes/"


class NotesListView(ListView):
    model = Notes
    context_object_name = "notes"
    template_name = "notes/notes_list.html"


class NotesDetailView(DetailView):
    model = Notes
    context_object_name = "note"
    template_name = "notes/notes_detail.html"
