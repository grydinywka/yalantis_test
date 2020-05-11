import logging
from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.http import HttpResponseNotFound
from django.contrib.sessions.models import Session
from django.views.decorators.csrf import csrf_exempt


class CounterView(TemplateView):
    template_name = "unique_counter/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.session.get('is_new_user', True):
            context['is_new_user'] = True
            self.request.session['is_new_user'] = False
            counter = 1
        else:
            context['is_new_user'] = False
            counter = 0
        counter += Session.objects.count()
        context['all'] = counter
        return context
    
    @csrf_exempt
    def dispatch(self, *args, **kwargs):
        if self.request.method != 'GET':
            logger = logging.getLogger(__name__)
            logger.error("Only GET method is allowed. You are using {}".format(self.request.method))
            return HttpResponseNotFound('Only GETs are allowed')
        return super().dispatch(*args, **kwargs)

