from django import forms
from .models import Book
from .models import myTodo

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ('title', 'publication_date', 'author', 'price', 'pages', 'book_type', )

class NameForm(forms.ModelForm):
    title = forms.CharField(label='Title', max_length=100)#widget=forms.TextInput(attrs={'class': 'special'}
    class Meta:
        ordering = ['id']
        model = myTodo
        fields = ('title',)
