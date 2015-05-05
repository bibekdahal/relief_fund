from django.shortcuts import render, get_object_or_404
from django.views.generic import View

from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse

from mainapp.models import *

class Index(View):

    def get(self,request):
        funds = Fund.objects.all()
        places = Place.objects.all()

        context = {'funds':funds, 'places':places}
        return render(request, 'index.html', context)

class Fund(View):

    def get(self, request):
        context = {}
        return render(request, 'fund.html', context)

    def post(self, request):
        context = {}
        provider_name = request.POST.get('provider_name')
        provider_phone = request.POST.get('provider_phone')
        provider = Provider.objects.filter(name=provider_name, phone=provider_phone)
        if not provider:
            provider = Provider(name=provider_name, phone=provider_phone)
            provider.save()

        place_name = request.POST.get('place')
        district_name = request.POST.get('district')
        latitude = request.POST.get('latitude')
        longitude = request.POST.get('longitude')
        place = Place.objects.filter(name=place_name)
        if not place:
            place = Place(name=place_name, district=district_name, latitude=latitude, longitude=longitude)
            place.save()

        return HttpResponseRedirect(reverse('mainapp:fund'))

