from django.shortcuts import render

from django.http import HttpResponseBadRequest

# Create your views here.

from .forms import *




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
        form = BaseInterForm(data=request.POST)

        if form.is_valid():
            form.save()
        else:
            return HttpResponseBadRequest('Данные не прошли валидацию')

        return render(request, 'tablem/base_detail.html', context={})
    else:
        return HttpResponseBadRequest('Метод запроса {} не поддерживается'.format(request.method))

def show_bases(request):
    pass