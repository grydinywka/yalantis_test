from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.http import HttpResponseNotFound
from django.contrib.sessions.models import Session


class CounterView(TemplateView):
    template_name = "unique_counter/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
#        print(dir(self.request.session), self.request.session.get_expiry_date())
        if self.request.session.get('is_new_user', True):
            context['is_new_user'] = True
            self.request.session['is_new_user'] = False
            # self.request.session.set_expiry(5)
            counter = 1
        else:
            context['is_new_user'] = False
            counter = 0
        counter += Session.objects.count()
        context['all'] = counter
        return context
    
    def dispatch(self, *args, **kwargs):
        if self.request.method != 'GET':
            return HttpResponseNotFound('Only GETs are allowed')
        return super().dispatch(*args, **kwargs)
