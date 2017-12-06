#from django.shortcuts import render
#from .models import Book
#from django.template.loader import render_to_string
#from .forms import BookForm


# Create your views here.
from .models import todoInfo
from .forms import NameForm
from django.shortcuts import render
from django.http import HttpResponseRedirect


#get_name

def index(request):
    #count_todo = todoInfo.objects.all()
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = NameForm(request.POST)
        # check whether it's valid:

        if form.is_valid():
            post = form.save(commit=False)
           # post.title = request.name_field
            post.save()
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            #return render(request, 'index.html', {'form': form})
            return HttpResponseRedirect(request.path)

    # if a GET (or any other method) we'll create a blank form
    else:
        form = NameForm()

    count_todo = todoInfo.objects.all().count()
    all_todo = todoInfo.objects.all()

    return render(request, 'index.html', {'form': form, 'count_todo': count_todo, 'all_todo': all_todo})

'''
def index(request):
    """
    Функция отображения для домашней страницы сайта.
    """
    # Генерация "количеств" некоторых главных объектов
   # num_books = Person.objects.all().count()
  #  num_instances = BookInstance.objects.all().count()
    # Доступные книги (статус = 'a')
   # num_instances_available = BookInstance.objects.filter(status__exact='a').count()
  #  num_authors = Author.objects.count()  # Метод 'all()' применен по умолчанию.

    # Отрисовка HTML-шаблона index.html с данными внутри
    # переменной контекста context
    return render(
        request,
        'index.html',
        context={}#{'num_books': num_books}# 'num_instances': num_instances,
                 #'num_instances_available': num_instances_available, 'num_authors': num_authors},
    )
'''

def book_list(request):
    books = Book.objects.all()
    return render(request, 'books/book_list.html', {'books': books})

def book_create(request):
    form = BookForm()
    context = {'form': form}
    html_form = render_to_string('books/includes/partial_book_create.html',
        context,
        request=request,
    )
    return JsonResponse({'html_form': html_form})
