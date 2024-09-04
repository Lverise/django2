from django.shortcuts import render

# Create your views here.
def renderTemplate(request):
    return render(request, 'templatesApp/pagina1.html')

def renderTemplate2(request):
    data = {"nombre": "Diego"}
    return render(request, 'templatesApp/pagina2.html', data)