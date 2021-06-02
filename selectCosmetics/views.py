from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from .models import Ages, Brands, Types, Prices, Cosmetics, Preferences

from random import randint

def index(request):
    ages_list = Ages.objects.all()
    brands_list = Brands.objects.all()
    types_list = Types.objects.all()
    prices_list = Prices.objects.all()
    template = loader.get_template('index.html')
    context = {
        'ages_list': ages_list,
        'brands_list': brands_list,
        'types_list': types_list,
        'prices_list': prices_list
    }
    return HttpResponse(template.render(context, request))

def selectedCosmetics(request, age_id, cosmetics_id):
    return HttpResponse("Wow you have selected %s cosmetics for %s age" % (cosmetics_id, age_id))

def select(request):
    try:
        age_id = request.POST['choice_age']
    except (KeyError):
        # Redisplay the question voting form.
        ages_list = Ages.objects.all()
        brands_list = Brands.objects.all()
        types_list = Types.objects.all()
        prices_list = Prices.objects.all()
        template = loader.get_template('index.html')
        context = {
            'ages_list': ages_list,
            'brands_list': brands_list,
            'types_list': types_list,
            'prices_list': prices_list,
            'error_message': "You didn't select an age!!!"
        }
        return HttpResponse(template.render(context, request))
    try:
        price_id = request.POST['choice_price']
    except (KeyError):
        # Redisplay the question voting form.
        ages_list = Ages.objects.all()
        brands_list = Brands.objects.all()
        types_list = Types.objects.all()
        prices_list = Prices.objects.all()
        template = loader.get_template('index.html')
        context = {
            'ages_list': ages_list,
            'brands_list': brands_list,
            'types_list': types_list,
            'prices_list': prices_list,
            'error_message': "You didn't select a price!!!"
        }
        return HttpResponse(template.render(context, request))
    
    brand_id = request.POST['choice_brand']
    type_id = request.POST['choice_type']
    all_preferences = Preferences.objects.filter(age=age_id).filter(cosmetics__price=price_id)
    if brand_id != '0':
        all_preferences = all_preferences.filter(cosmetics__brand=brand_id)
    if type_id != '0':
        all_preferences = all_preferences.filter(cosmetics__type=type_id)
    if not all_preferences:
        return HttpResponse("No data for given params")
    
    return HttpResponse(str(all_preferences[randint(0, all_preferences.count() - 1)]))