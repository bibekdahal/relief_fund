from django.shortcuts import render, get_object_or_404
from django.views.generic import View

from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse

from mainapp.models import *

class Index(View):

    def get(self,request):
        context = {}
        return render(request, 'index.html', context)
