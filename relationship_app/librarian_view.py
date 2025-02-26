from django.shortcuts import render
from django.contrib.auth.decorators import user_passes_test
from .models import user_is_librarian

@user_passes_test(user_is_librarian)
def librarian_view(request):
    return render(request, 'relationship_app/librarian_view.html')
