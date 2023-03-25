from django.shortcuts import render

from django.shortcuts import render


def index(request):
    return render(request, 'main/index.html')


def about1(request):
    return render(request, 'main/about.html')

    # data = {
    #     'title': 'Bosh sahifa',
    #     'values': ['Some', 'Heloo', '243242'],
    #     'obj': {
    #         'car': 'BMW',
    #         'age': 18,
    #         'hobby': 'football'
    #     }
    # }
