from django.db import models

# Create your models here.




'''
Заголовки таблицы
#    Data    Проект    Цена    Номеров    Использовали    Остаток    Источник    Как собиралась    Ответственный    link    Status    Comment    Цена номера


Что необходимо сделать? По сути повторить функционал гугл таблиц.
Страница для импорта базы (либо из csv \ txt, либо из поля в которую номера вставляются списком),
 с проставлением параметров (дата, проект, цена, источник, как собиралась, ответственный)
Страница с отображением всех импортированных баз, с возможностью фильтрации по параметрам

Хотелось бы увидеть
Django + sqlite\ posgresql + шаблонизаторы + хороший код
'''


class BaseInter(models.Model):
    '''
    Характеристики контактной базы
    Расширение BaseMain

    '''

    date = models.DateField('Дата загрузки')
    project = models.CharField('Название проекта', max_length=60)
    price = models.PositiveIntegerField('Стоимость базы')
    amount_total = models.PositiveIntegerField('Кол-во всех контактов', null=True)
    amount_used = models.PositiveIntegerField('Кол-во использованных контактов', null=True)
    amount_left = models.PositiveIntegerField('Кол-во оставшихся контактов', null=True)


    source = models.CharField('Источник', max_length=200)
    source_params = models.CharField('Как собиралась', max_length=200)
    name_accountable = models.CharField('Имя ответственного', max_length=60)
    status = models.BooleanField('Статус', default=False)
    comment = models.CharField('Комментарий', max_length=200, null=True)
    number_price = models.FloatField('Стоимость одного номера', null=True)

    link = models.FileField('link', upload_to='documents/')



    def __str__(self):
        return '%s (%s)' % (self.project, self.link)

    class Meta:
        verbose_name = 'Контактная База'
        verbose_name_plural = 'Контактные Базы'


class BaseMain(models.Model):
    '''
    Контакты
    Какие поля у контакта?
    '''

    base = models.ForeignKey(BaseInter, on_delete=models.CASCADE, related_name='contacts')

    name = models.CharField('Имя', max_length=60, null=True)
    email = models.EmailField('email', null=True)
    telephon = models.CharField('Номер телефона', max_length=60, null=True)
    comment = models.TextField('Комментарий', null=True)

    def __str__(self):
        return '%s' % self.id

    class Meta:
        verbose_name = '<Контакт>'
        verbose_name_plural = '<Контакты>'