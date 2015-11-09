from django.shortcuts import render_to_response
from django.template import RequestContext
from django.views.decorators.csrf import csrf_exempt
from car.models import Car

@csrf_exempt
def SfvueCars(request):
        cars = Car.objects.all().order_by('name')
        context = {'cars': cars}
        return render_to_response('sfvueCars.html')


