# from django.shortcuts import render
# from django.http import Http404
from django.views.generic import CreateView, DetailView, ListView, UpdateView

from .forms import NotesForm
from .models import Notes


class NotesCreateView(CreateView):
    model = Notes
    success_url = '/smart/notes'
    # form_class can be passed instead of 'fields' to allow for more powerful validation
    form_class = NotesForm


class NotesUpdateView(UpdateView):
    model = Notes
    success_url = '/smart/notes'
    form_class = NotesForm


class NotesListView(ListView):
    model = Notes
    context_object_name = "notes"
    template_name = "notes/notes_list.html"


class NotesDetailView(DetailView):
    model = Notes
    context_object_name = "note"

# This "function-based view" has been replaced with the NotesListView class to make this a "class based view"
# def detail(request, pk):  # pk = private key
#     try:
#         note = Notes.objects.get(pk=pk)
#     except Notes.DoesNotExist:
#         raise Http404("Note doesn't exist")
#     return render(request, 'notes/notes_detail.html', {'note': note})
