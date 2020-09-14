from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Event, User

def index(request):
    template = loader.get_template('deck/index.html')
    all_events = Event.objects.all()
    list = []
    for dates in all_events:
        temp = str(dates.due_date).split('-')
        temp.reverse()
        list.append('/'.join(temp))
    context = {
        'all_events': all_events,
        'list_date': list,
    }
    return HttpResponse(template.render(context, request))


def new_event(request):
    template = loader.get_template('deck/newevent.html')
    context = ''
    return HttpResponse(template.render(context, request))

def profile(request):
    template = loader.get_template('deck/profile.html')
    context = ''
    return HttpResponse(template.render(context, request))
