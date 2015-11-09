from django.shortcuts import render_to_response
from django.template import RequestContext
from car.models import Car
from car.models import Make

def CarsAll(request):
    cars = Car.objects.all().order_by('name')
    context = {'cars': cars}
    return render_to_response('carsall.html',context, context_instance=RequestContext(request))

def index(request):
    return render_to_response('index.html')

def SpecificCar(request, carslug):
    c = Car.objects.get(slug=carslug)
    context = {'car': c}
    return render_to_response('singlecar.html', context, context_instance=RequestContext(request))

def SpecificMake(request, makeslug):
    m = Make.objects.get(slug=makeslug)
    cars = Car.objects.filter(make=m)
    context = {'cars': cars}
    return render_to_response('singlemake.html', context, context_instance=RequestContext(request))
