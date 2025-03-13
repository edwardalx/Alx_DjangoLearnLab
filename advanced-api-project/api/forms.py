from django import forms

from .models import Book, Author

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = '__all__'
  #this part of the code is useful if you want to verify  like we do in serializers    
    author = forms.ModelChoiceField(queryset=Author.objects.all(), required=True)

    def clean_author(self):
        author = self.cleaned_data['author']
        if not author.is_verified:
            raise forms.ValidationError("You cannot select an unverified author.")
        return author