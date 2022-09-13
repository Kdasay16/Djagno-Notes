# from django.shortcuts import render
from django.http.response import HttpResponseRedirect
from django.views.generic import CreateView, DetailView, ListView, UpdateView
from django.views.generic.edit import DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin

from .forms import NotesForm
from .models import Notes


class NotesCreateView(CreateView):
    model = Notes
    success_url = '/smart/notes'
    # form_class can be passed instead of 'fields' to allow for more powerful validation
    form_class = NotesForm
    login_url = "/admin"

    def form_valid(self, form):
        # commit=False creates the object, but doesn't save it to the database
        # this way we can insert the user before it goes to the database
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())


class NotesUpdateView(UpdateView):
    model = Notes
    success_url = '/smart/notes'
    form_class = NotesForm
    login_url = "/admin"


class NotesDeleteView(DeleteView):
    model = Notes
    success_url = '/smart/notes'
    login_url = "/admin"


class NotesListView(LoginRequiredMixin, ListView):
    model = Notes
    context_object_name = "notes"
    template_name = "notes/notes_list.html"
    login_url = "/admin"

    def get_queryset(self):  # get_queryset is a django method, used to get all USER notes
        return self.request.user.notes.all()


class NotesDetailView(DetailView):
    model = Notes
    context_object_name = "note"
    login_url = "/admin"

# This "function-based view" has been replaced with the NotesListView class to make this a "class based view"
# def detail(request, pk):  # pk = private key
#     try:
#         note = Notes.objects.get(pk=pk)
#     except Notes.DoesNotExist:
#         raise Http404("Note doesn't exist")
#     return render(request, 'notes/notes_detail.html', {'note': note})
