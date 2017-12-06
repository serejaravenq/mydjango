from django import forms
from .models import Book
from .models import todoInfo

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ('title', 'publication_date', 'author', 'price', 'pages', 'book_type', )

class NameForm(forms.ModelForm):

    class Meta:
        model = todoInfo
        fields = ('title',)
