from django.shortcuts import render, redirect

from django.http import HttpResponseBadRequest

import datetime

# Create your views here.
from .forms import *
from django.db.models import Q

def base_upload(request):
    '''
    Отображает форму добавления базы контактов(GET)
    Сохраняет оформленную базу(POST)
    :param request:
    :return:
    '''

    if request.method == 'GET':
        base_form = BaseInterForm()
        return render(request, 'tablem/base_upload.html', context={'base_form':base_form})
    elif request.method == 'POST':
        print(request.FILES)
        form = BaseInterForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        else:
            return HttpResponseBadRequest('Данные не прошли валидацию')
        return redirect('/tablem/show_bases')
    else:
        return HttpResponseBadRequest('Метод запроса {} не поддерживается'.format(request.method))

def show_bases(request):

    if request.method == 'GET':
        fields = [field for field in BaseInter._meta.get_fields()]

        if 'qwery' in request.GET:
            qwery = request.GET.get('qwery')

            bases = BaseInter.objects.filter(Q(project__icontains=qwery)
                                             | Q(name_accountable__icontains=qwery)
                                             | Q(source__icontains=qwery)
                                             | Q(source_params__icontains=qwery)
                                             | Q(comment__icontains=qwery)
                                             )
            return render(request, 'tablem/base_detail.html', context={'bases': bases, 'fields': fields})


        elif ('date_start' in request.GET) and ('date_end'in request.GET):
            date_start = datetime.datetime.strptime(request.GET.get('date_start'), '%Y-%m-%d')
            date_end = datetime.datetime.strptime(request.GET.get('date_end'), '%Y-%m-%d')
            bases = BaseInter.objects.filter(Q(date__gt=date_start) & Q(date__lt=date_end))

            return render(request, 'tablem/base_detail.html', context={'bases': bases, 'fields': fields})



        else:
            bases = BaseInter.objects.all()
            return render(request, 'tablem/base_detail.html', context={'bases': bases, 'fields': fields})


