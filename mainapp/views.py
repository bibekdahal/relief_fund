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

    def get(self, request, fund_id=None):
        context = {}
        itemtypes = ItemType.objects.all()
        context['itemtypes'] = itemtypes

        if not fund_id:
            place = request.GET.get('place')
            lat = request.GET.get('lat')
            lon = request.GET.get('lon')
            if place:
                context['place'] = place
            if lat:
                context['lat'] = int(lat)
            if lon:
                context['lon'] = int(lon)
            return render(request, 'fund.html', context)
        else:
            fund = get_object_or_404(Fund, pk=fund_id)
            context['fund'] = fund
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
            itemtype_check = request.POST.get(itemtype.name)
            if itemtype_check:
                remarks = request.POST.get(itemtype.name+"_remarks")
                item = Item(type=itemtype, remarks=remarks, fund=fund)
                item.save()

        return HttpResponseRedirect(reverse('mainapp:fund'))





