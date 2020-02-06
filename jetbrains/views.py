from django.http import HttpResponse


def hello(request):

    print('test')

    print('test 2')

    return HttpResponse('hello')
