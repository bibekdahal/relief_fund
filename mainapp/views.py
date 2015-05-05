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

class FundView(View):

    def get(self, request):
        context = {}
        itemtypes = ItemType.objects.all()
        context['itemtypes'] = itemtypes
        return render(request, 'fund.html', context)

    def post(self, request):
        context = {}
        provider_name = request.POST.get('provider_name')
        provider_phone = request.POST.get('provider_phone')
        provider = Provider.objects.filter(name=provider_name, phone=provider_phone)
        if provider:
            provider = provider[0]
        if not provider:
            provider = Provider(name=provider_name, phone=provider_phone)
            provider.save()

        place_name = request.POST.get('place')
        district_name = request.POST.get('district')
        latitude = request.POST.get('latitude')
        longitude = request.POST.get('longitude')
        place = Place.objects.filter(name=place_name)
        if place:
            place = place[0]
        if not place:
            place = Place(name=place_name, district=district_name, latitude=latitude, longitude=longitude)
            place.save()

        fundstate = int(request.POST.get("fundstate"))
        fund = Fund(provider=provider, place=place, state=fundstate)
        fund.save()

        itemtype_list = ItemType.objects.all()
        for itemtype in itemtype_list:
            amount = int(request.POST.get(itemtype.name+"_amount"))
            if amount>0:
                item = Item(type=itemtype, amount=amount, fund=fund)
                item.save()

        return HttpResponseRedirect(reverse('mainapp:fund'))





