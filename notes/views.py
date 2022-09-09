# from django.shortcuts import render
# from django.http import Http404
from django.views.generic import DetailView, ListView

from .models import Notes


class NotesListView(ListView):
    model = Notes
    context_object_name = "notes"
    template_name = "notes/notes_list.html"

# This has been replaced with the NotesListView class to make this a "class based view"
# def list(request):
#     all_notes = Notes.objects.all()
#     return render(request, 'notes/notes_list.html', {'notes': all_notes})


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
