# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    # response = "hello"
    # return HttpResponse(response)
    return render(request, "django_portfolio/index.html")

def testimonials(request):
    print(request.method)
    return render(request, "django_portfolio/testimonials.html")
