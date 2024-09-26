from django.shortcuts import render

def index(request):
    return render(request, 'menu/index.html')




# from django.views.generic import TemplateView
#
#
# class IndexView(TemplateView):
#     template_name = 'menu/index.html'
