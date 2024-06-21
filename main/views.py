from django.shortcuts import render

# Create your views here.


def main_view(request):

    context = {"object": 'main'}
    return render(request, 'main/test.html', context=context)
