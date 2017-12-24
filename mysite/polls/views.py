#from django.shortcuts import render
#from .models import Book
#from django.template.loader import render_to_string
#from .forms import BookForm
#from django.views.decorators.csrf import csrf_exempt
#import json.JSONEncoder
from django.http import HttpResponse
#from django.http import HttpResponseRedirect
from django.http import JsonResponse
#from django.utils.decorators import method_decorator
#from django.core import serializers
#from django.forms.models import modelform_factory
#from django.http import QueryDict

import json
from django.views.generic import View
from .models import myTodo
from .forms import NameForm
from django.shortcuts import render, redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def all(request):

    return JsonResponse('ok', safe=False)
# Create your views here.
class RestView(View):

    def delAll(request):
        if request.method == "PUT":
            data = json.loads(request.body.decode('UTF-8'))
            print(data)
            #title = data.get('title')
            event = data.get('idevent')
            content = myTodo.objects.all().filter(active=False).delete()

            for i in content:
                print(i)

            if event == 'all':
                all_todo = myTodo.objects.all().order_by('id')
                template = 'index.html'

            elif event == 'unchecked':
                all_todo = myTodo.objects.filter(active=True).order_by('id')
                template = 'unchecked.html'

            elif event == 'checked':
                all_todo = myTodo.objects.filter(active=False).order_by('id')
                template = 'checked.html'

            check_todo = myTodo.objects.filter(active=True).count()
            uncheck_todo = myTodo.objects.filter(active=False).count()
            paginator = Paginator(all_todo, 5)

            form = NameForm()

            currentpage = data.get('currentpage')

            if currentpage == None:
                page = paginator.num_pages
            else:
                page = currentpage

            try:
                pages = paginator.page(page)
            except PageNotAnInteger:
                pages = paginator.page(1)
            except EmptyPage:
                pages = paginator.page(paginator.num_pages)

            pages.event = event

            return render(request, template,
                     {'pages': pages,'form': form,
                      'check_todo': check_todo, 'uncheck_todo': uncheck_todo})

    def onAll(request):
        if request.method == "PUT":
            data = json.loads(request.body.decode('UTF-8'))
            print(data)
            #title = data.get('title')
            event = data.get('idevent')
            myTodo.objects.all().update(active=False)
            if event == 'all':
                all_todo = myTodo.objects.all().order_by('id')
                template = 'index.html'

            elif event == 'unchecked':
                all_todo = myTodo.objects.filter(active=True).order_by('id')
                template = 'unchecked.html'

            elif event == 'checked':
                all_todo = myTodo.objects.filter(active=False).order_by('id')
                template = 'checked.html'

            check_todo = myTodo.objects.filter(active=True).count()
            uncheck_todo = myTodo.objects.filter(active=False).count()
            paginator = Paginator(all_todo, 5)

            form = NameForm()

            currentpage = data.get('currentpage')

            if currentpage == None:
                page = paginator.num_pages
            else:
                page = currentpage

            try:
                pages = paginator.page(page)
            except PageNotAnInteger:
                pages = paginator.page(1)
            except EmptyPage:
                pages = paginator.page(paginator.num_pages)

            pages.event = event

            return render(request, template,
                     {'pages': pages,'form': form,
                      'check_todo': check_todo, 'uncheck_todo': uncheck_todo})

    def offAll(request):
        if request.method == "PUT":
            data = json.loads(request.body.decode('UTF-8'))
            print(data)
            #title = data.get('title')
            event = data.get('idevent')
            myTodo.objects.all().update(active=True)
            if event == 'all':
                all_todo = myTodo.objects.all().order_by('id')
                template = 'index.html'

            elif event == 'unchecked':
                all_todo = myTodo.objects.filter(active=True).order_by('id')
                template = 'unchecked.html'

            elif event == 'checked':
                all_todo = myTodo.objects.filter(active=False).order_by('id')
                template = 'checked.html'

            check_todo = myTodo.objects.filter(active=True).count()
            uncheck_todo = myTodo.objects.filter(active=False).count()
            paginator = Paginator(all_todo, 5)

            form = NameForm()

            currentpage = data.get('currentpage')

            if currentpage == None:
                page = paginator.num_pages
            else:
                page = currentpage

            try:
                pages = paginator.page(page)
            except PageNotAnInteger:
                pages = paginator.page(1)
            except EmptyPage:
                pages = paginator.page(paginator.num_pages)

            pages.event = event

            return render(request, template,
                     {'pages': pages,'form': form,
                      'check_todo': check_todo, 'uncheck_todo': uncheck_todo})

    def all(request):
        check_todo = myTodo.objects.filter(active=True).count()
        uncheck_todo = myTodo.objects.filter(active=False).count()
        all_todo = myTodo.objects.all().order_by('id')
        paginator = Paginator(all_todo, 5)
        page = request.GET.get('page')

        form = NameForm()
        try:
            pages = paginator.page(paginator.num_pages)#page
        except PageNotAnInteger:
            pages = paginator.page(1)
        except EmptyPage:
            pages = paginator.page(paginator.num_pages)

        path = request.path.split('/')
        event = path[2]
        pages.event = event

        return render(request, 'index.html',
                {'pages': pages,'form': form,
                'check_todo': check_todo, 'uncheck_todo': uncheck_todo})


    def checked(request):
        check_todo = myTodo.objects.filter(active=True).count()
        uncheck_todo = myTodo.objects.filter(active=False).count()
        all_todo = myTodo.objects.all().filter(active=False).order_by('id')


        paginator = Paginator(all_todo, 5)

        page = request.GET.get('page')

        if page == None:
                page = paginator.num_pages
        form = NameForm()

        try:
            pages = paginator.page(page)#page
        except PageNotAnInteger:
            pages = paginator.page(1)
        except EmptyPage:
            pages = paginator.page(paginator.num_pages)

        path = request.path.split('/')
        event = path[2]
        pages.event = event

        return render(request, 'checked.html',
                {'pages': pages,'form': form,
                'check_todo': check_todo, 'uncheck_todo': uncheck_todo})


    def unchecked(request):
        check_todo = myTodo.objects.filter(active=True).count()
        uncheck_todo = myTodo.objects.filter(active=False).count()

        all_todo = myTodo.objects.filter(active=True).order_by('id')

        paginator = Paginator(all_todo, 5)
        page = request.GET.get('page')

        form = NameForm()

        try:
            pages = paginator.page(paginator.num_pages)#page
        except PageNotAnInteger:
            pages = paginator.page(1)
        except EmptyPage:
            pages = paginator.page(paginator.num_pages)

        path = request.path.split('/')
        event = path[2]
        pages.event = event

        return render(request, 'unchecked.html',
                {'pages': pages,'form': form,
                'check_todo': check_todo, 'uncheck_todo': uncheck_todo})


    def get(request):
        if request.method == "GET":
            event = request.GET.get('filter')

            if event == None:
                event = 'all'
            if event == '':
                event = 'all'
            print(event)

            if event == 'all':
                all_todo = myTodo.objects.all().order_by('id')
                template = 'index.html'
            elif event == 'checked':
                all_todo = myTodo.objects.filter(active=False).order_by('id')
                template = 'checked.html'
            elif event == 'unchecked':
                all_todo = myTodo.objects.filter(active=True).order_by('id')
                template = 'unchecked.html'

            check_todo = myTodo.objects.filter(active=True).count()
            uncheck_todo = myTodo.objects.filter(active=False).count()

            paginator = Paginator(all_todo, 5)
            page = request.GET.get('page')

            if page == None:
                page = paginator.num_pages

            form = NameForm()
            try:
                pages = paginator.page(page)#page
            except PageNotAnInteger:
                pages = paginator.page(1)
            except EmptyPage:
                pages = paginator.page(paginator.num_pages)


            pages.event = event

            return render(request, template,
                     {'pages': pages,'form': form,
                      'check_todo': check_todo, 'uncheck_todo': uncheck_todo})

    def post(request):
        if request.method == "POST":
            array = json.loads(request.body.decode('UTF-8'))
            request.POST = array[0]
            event = array[1]

            if event == 'all':
                all_todo = myTodo.objects.all().order_by('id')
                template = 'index.html'
            elif event == 'unchecked':
                all_todo = myTodo.objects.filter(active=True).order_by('id')
                template = 'unchecked.html'
            elif event == 'checked':
                all_todo = myTodo.objects.filter(active=False).order_by('id')
                template = 'checked.html'

            form = NameForm(request.POST)
            if form.is_valid():
                form.save()


            check_todo = myTodo.objects.filter(active=True).count()
            uncheck_todo = myTodo.objects.filter(active=False).count()
            page = request.GET.get('page')
            paginator = Paginator(all_todo, 5)

            try:
                pages = paginator.page(paginator.num_pages)
            except PageNotAnInteger:
                pages = paginator.page(1)
            except EmptyPage:
                pages = paginator.page(paginator.num_pages)

            pages.event = event

            return render(request, template,
                     {'pages': pages,
                      'form': form,
                      'check_todo': check_todo, 'uncheck_todo': uncheck_todo})

    def update(request, id):
         if request.method == "PUT":
            data = json.loads(request.body.decode('UTF-8'))
            print(data)
            title = data.get('title')
            event = data.get('idevent')

            if event == 'all':
                all_todo = myTodo.objects.all().order_by('id')
                template = 'index.html'

            elif event == 'unchecked':
                all_todo = myTodo.objects.filter(active=True).order_by('id')
                template = 'unchecked.html'

            elif event == 'checked':
                all_todo = myTodo.objects.filter(active=False).order_by('id')
                template = 'checked.html'

            print(event)
            myTodo.objects.filter(id=id).update(title=title)

            check_todo = myTodo.objects.filter(active=True).count()
            uncheck_todo = myTodo.objects.filter(active=False).count()
            paginator = Paginator(all_todo, 5)

            form = NameForm()

            currentpage = data.get('currentpage')

            if currentpage == None:
                page = paginator.num_pages
            else:
                page = currentpage

            try:
                pages = paginator.page(page)
            except PageNotAnInteger:
                pages = paginator.page(1)
            except EmptyPage:
                pages = paginator.page(paginator.num_pages)

            pages.event = event

            return render(request, template,
                     {'pages': pages,'form': form,
                      'check_todo': check_todo, 'uncheck_todo': uncheck_todo})

    def put(request, id):
        if request.method == "PUT":

            data = json.loads(request.body.decode('UTF-8'))
            print(data)
            status = data.get('status')
            status = True if status == 'true' else False
            event = data.get('idevent')
            print(event)
            if event == 'all':
                all_todo = myTodo.objects.all().order_by('id')
                template = 'index.html'
            elif event == 'unchecked':
                all_todo = myTodo.objects.filter(active=True).order_by('id')
                template = 'unchecked.html'
            elif event == 'checked':
                all_todo = myTodo.objects.filter(active=False).order_by('id')
                template = 'checked.html'

            myTodo.objects.filter(id=id).update(active=status)
            form = NameForm()

            check_todo = myTodo.objects.filter(active=True).count()
            uncheck_todo = myTodo.objects.filter(active=False).count()
            paginator = Paginator(all_todo, 5)

            idget = data.get('strget')
            currentpage = data.get('currentpage')

            if currentpage == None:
                page = paginator.num_pages
            else:
                page = currentpage
            print(page)
            try:
                pages = paginator.page(page)
            except PageNotAnInteger:
                pages = paginator.page(1)
            except EmptyPage:
                pages = paginator.page(paginator.num_pages)
            pages.event = event

            return render(request, template,
                     {'pages': pages,'form': form,
                      'check_todo': check_todo, 'uncheck_todo': uncheck_todo})

    def delete(request, id):
    # delete an object and send a confirmation response
        if request.method == "DELETE":

                data = json.loads(request.body.decode('UTF-8'))
                myTodo.objects.get(id=id).delete()
                event = data.get('idevent')
                print(event)
                if event == 'all':
                    all_todo = myTodo.objects.all().order_by('id')
                    template = 'index.html'
                elif event == 'unchecked':
                    all_todo = myTodo.objects.filter(active=True).order_by('id')
                    template = 'unchecked.html'
                elif event == 'checked':
                    all_todo = myTodo.objects.filter(active=False).order_by('id')
                    template = 'checked.html'

                check_todo = myTodo.objects.filter(active=True).count()
                uncheck_todo = myTodo.objects.filter(active=False).count()
                page = request.GET.get('page')
                paginator = Paginator(all_todo, 5)
                form = NameForm()
                idget = data.get('strget')

                if idget == 'None':
                   page = paginator.num_pages
                else:
                    result = idget.split('&')
                    page = result[0].split('=')[1]

                try:
                    pages = paginator.page(page)
                except PageNotAnInteger:
                    pages = paginator.page(1)
                except EmptyPage:
                    pages = paginator.page(paginator.num_pages)

                return render(request, template,
                         {'pages': pages,'form': form,
                          'check_todo': check_todo, 'uncheck_todo': uncheck_todo})







