"""platzigram views"""
#django
from django.http import HttpResponse

#utilidades
from datetime import datetime


def hello_world(request):
    now = datetime.now().strftime('%b %dth, %Y - %H:%M hrs')
    return HttpResponse('Oh , hi! Current server time is {now}'
                        .format(now=str(now))
                        )


def hi(request):
    import pdb; pdb.set_trace()
    return HttpResponse('Hi!')