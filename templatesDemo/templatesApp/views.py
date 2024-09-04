from django.shortcuts import render

# Create your views here.
def renderTemplate(request):
    return render(request, 'templatesApp/pagina1.html')

def renderTemplate2(request):
    data = {"nombre": "Junior 'Mbappé Fernández", "id":123, "email":"diego.holala@gmail.com",}
    return render(request, 'templatesApp/pagina2.html', data)