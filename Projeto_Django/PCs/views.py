from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import CreateView, DeleteView, UpdateView, DetailView
from .models import Desktop
from .forms import DesktopModelForm

# Listagem
def PCs_view(request):
    desktops = Desktop.objects.all()
    search = request.GET.get('search')

    if search:
        desktops = Desktop.objects.filter(Processador__icontains = search)
    return render(request, 
                  'PCs.html',
                  {'desktops' : desktops})
    

def sobre_view(request):
    return render(request, 'sobre.html')
# Cadastro

def cadastro_view(request):
    return render(request, 'cadastro.html')
   

# Formulário em baseview
class DesktopCreateView(CreateView):
    model = Desktop
    form_class = DesktopModelForm
    template_name = 'new_desktop.html'
    success_url = '/PCs/'


class DesktopDeleteView(DeleteView):
    model = Desktop
    template_name = "desktop_delete.html"
    success_url = '/PCs/'

class DesktopUpdateView(UpdateView):
    model = Desktop
    form_class = DesktopModelForm
    template_name = "desktop_update.html"
    success_url = '/PCs/'


class DesktopDetailView(DetailView):
    model = Desktop
    template_name = 'desktop_detail.html'



#Em detalhes
#<a href= "{% url 'desktop_delete' pk= object.pk }" class=" btn btn-prymary"> Deletar</a>
#<a href= "{% url 'desktop_update' pk= object.pk }" class=" btn btn-prymary"> Atualizar</a>
