from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from .forms import NoteForm
from .models import Note

# Create your views here.
class NoteListView(ListView):
    model = Note
    template_name = "notes_system/note_list.html"
    context_object_name = "notes"

class NoteDetailView(DetailView):
    model = Note
    template_name = "notes_system/note_detail.html"
    context_object_name = "note"

def add_note(request):
    if request.method == 'POST':
        form = NoteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('note-list')
    else:
        form = NoteForm()

    return render(request, "notes_system/add_note.html", {'form': form})