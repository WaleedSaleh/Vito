from django.shortcuts import render,HttpResponse,redirect
from .forms import BusForm
from .models import Bus
from django.views.generic import ListView,DetailView

# Create your views here.

def index(request):
    return render(request, 'vitoapp/index.html', context={'title': "Home"})


def add_vito(request):
    if request.method == 'POST':
        form = BusForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('vito:vitos')
        else:
            return HttpResponse('Something went wrong, please check your data')
    else:
        form = BusForm
    return render(request,'vitoapp/add-vito.html',context={'form':form,
                                                    'title':'Add Vito'})


class BusListView(ListView):
    model = Bus
    template_name = 'vitoapp/vitos_list.html'
    context_object_name = 'vitos'


class BusDetailView(DetailView):
    model = Bus
    template_name = 'vitoapp/bus_detail.html'
    context_object_name = 'vito_detail'






