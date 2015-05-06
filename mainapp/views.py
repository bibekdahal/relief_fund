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
                context['lat'] = float(lat)
            if lon:
                context['lon'] = float(lon)
            return render(request, 'fund.html', context)
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
        
        # if update then fund_id exist
        if fund_id:
            # get our fund object to update
            fund_obj = Fund.objects.get(id=fund_id)
            # get all the items associated with fund
            items = Item.objects.filter(fund=fund_obj)

            # for debugging
            tempstring = ''
            for itemtype in itemtype_list:
                itemtype_check = request.POST.get(itemtype.name)
                if itemtype_check:
                    tempstring += ' '+itemtype.name
                    remarks = request.POST.get(itemtype.name+"_remarks").strip()

            #return HttpResponse(tempstring)

            # get the provider for this fund and update it
            provider = fund_obj.provider
            provider.name = provider_name
            provider.phone = provider_phone
            provider.save()

            # update undsate too
            fund_obj.state = fundstate    
            #finally save the fund -> updated
            fund_obj.save()
            return HttpResponseRedirect(reverse('mainapp:fund'))


        #else just create new fund 
        else:
            provider = Provider.objects.filter(name=provider_name, phone=provider_phone)
            if provider:
                provider = provider[0]
            if not provider:
                provider = Provider(name=provider_name, phone=provider_phone)
                provider.save()

            place = Place.objects.filter(name=place_name)
            if place:
                place = place[0]
            if not place:
                place = Place(name=place_name, district=district_name, latitude=latitude, longitude=longitude)
                place.save()

            fund = Fund(provider=provider, place=place, state=fundstate)
            fund.save()

            for itemtype in itemtype_list:
                itemtype_check = request.POST.get(itemtype.name)
                if itemtype_check:
                    remarks = request.POST.get(itemtype.name+"_remarks").strip()
                    item = Item(type=itemtype, remarks=remarks, fund=fund)
                    item.save()

            return HttpResponseRedirect(reverse('mainapp:fund'))




