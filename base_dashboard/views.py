from django.shortcuts import render

# Create your views here.
def base_dashboard(request):
    template_name = 'base.html'
    return render(request, template_name)