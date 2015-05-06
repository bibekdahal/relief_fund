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


        if request.GET.get('buffer') == 1:
            isbuffer = True
        else:
            isbuffer = False
        context['isbuffer'] = isbuffer

        if not fund_id:
            place = request.GET.get('place')
            lat = request.GET.get('lat')
            lon = request.GET.get('lon')
            if place:
                context['place'] = place
            if lat:
                context['lat'] = float(lat)
            if lon:
                context['lon'] = float(lon)
            return render(request, 'fund.html', context)
        else:
            if isbuffer:
                fund = get_object_or_404(Buffer, pk=fund_id)
                items = BufferItem.objects.filter(fund=fund)
            else:
                fund = get_object_or_404(Fund, pk=fund_id)
                items = Item.objects.filter(fund=fund)

            context['fund'] = fund
            context['items'] = items
            return render(request, 'fund.html', context)

    def post(self, request, fund_id=None):
        context = {}
        itemtype_list = ItemType.objects.all()

        provider_name = request.POST.get('provider_name').strip()
        provider_phone = request.POST.get('provider_phone')
        fundstate = int(request.POST.get("fundstate"))
        place_name = request.POST.get('place').strip()
        district_name = request.POST.get('district').strip()
        latitude = request.POST.get('latitude')
        longitude = request.POST.get('longitude')
        
        if not provider_name is None and not provider_name == "":
            provider = Provider.objects.filter(name=provider_name, phone=provider_phone)
            if provider:
                provider = provider[0]
            if not provider:
                provider = Provider(name=provider_name, phone=provider_phone)
                provider.save()
        else:
            provider = None

        place = Place.objects.filter(name=place_name)
        if place:
            place = place[0]
        if not place:
            place = Place(name=place_name, district=district_name, latitude=latitude, longitude=longitude)
            place.save()
        
        if request.GET.get('buffer') == 1:
            isbuffer = True
        else:
            isbuffer = False
        if not isbuffer:
            if fund_id:
                fund = get_object_or_404(Fund, pk=fund_id)
            else:
                fund = None
            bufferfund = Buffer(provider=provider, place=place, state=fundstate, fund=fund)
        else:
            bufferfund = get_object_or_404(Buffer, pk=fund_id)
            bufferfund.state = fundstate
            bufferfund.provider = provider
            bufferfund.place = place
            BufferItem.objects.filter(fund=bufferfund).delete()

        bufferfund.save()

        for itemtype in itemtype_list:
            itemtype_check = request.POST.get(itemtype.name)
            if itemtype_check:
                remarks = request.POST.get(itemtype.name+"_remarks").strip()
                item = BufferItem(type=itemtype, remarks=remarks, fund=bufferfund)
                item.save()

        if isbuffer:
            ReviewBuffer(bufferfund)

        return HttpResponseRedirect(reverse('mainapp:index'))

def ReviewBuffer(bufferfund):
    if bufferfund.fund:
        fund = bufferfund.fund
        fund.provider = bufferfund.provider
        fund.place = bufferfund.place
        fund.state = bufferfund.state
    else:
        fund = Fund(provider=bufferfund.provider, place=bufferfund.place, state=bufferfund.state)
    
    items = Item.objects.filter(fund=fund).delete()
    fund.save()

    bufferitems = BufferItem.objects.filter(fund=bufferfund)
    for it in bufferitems:
        item = Item(type=it.type, remarks=it.remarks, fund=fund)
        item.save()

    bufferitems.delete()
    bufferfund.delete()
