# from django.shortcuts import render
from django.views.generic import TemplateView
from django.shortcuts import render

# Create your views here.
from . import forms
from . import models as m


class IndexView(TemplateView):
    template_name = 'books/index.djhtml'
    model = m.Media

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(make_default_table())
        return context


def dispatch(request):
    return render(request, 'books/index.djhtml',
                  make_default_table(
                      form=forms.QueryForm(),
                      error_message='Invalid input!'))


def make_default_table(form=forms.QueryForm(), error_message=''):
    return {'book_list': [],
            'form': form,
            'error_message': error_message,
            }
