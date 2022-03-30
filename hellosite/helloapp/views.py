from django.shortcuts import render

from django.views import View

#Create your views here.
class HelloWorldView(View):
    def get(self, request):
        return render(request=request, template_name='hello_world.html')


class HelloNameView(View):
    def get(self, request, name):
        context = {'url_name': name}
        return render(request=request, template_name='hello_name.html', context=context)


class GoodbyeDjangoView(View):
    def get(self, request, name):
        context = {'url_name': name}
        return render(request=request, template_name='goodbye_django.html', context=context)