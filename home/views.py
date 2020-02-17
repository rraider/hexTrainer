from django.shortcuts import render

# Create your views here.
def start_view(request):
    template_name = 'start.html'

    return render(request, template_name, {})
