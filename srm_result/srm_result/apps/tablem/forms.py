

from django.forms import ModelForm
from tablem.models import *

from django import forms

import datetime



class DateInput(forms.DateInput):
    input_type = 'date'



class BaseInterForm(ModelForm):

    link = forms.FileField()


    class Meta:
        model = BaseInter
        fields = ['date', 'project', 'price',
                  'source', 'source_params',
                  'name_accountable',
                  'link']
        widgets = {'date': DateInput()}



    def save(self, *args, **kwargs):

        super(BaseInterForm, self).save(self, *args, **kwargs)



