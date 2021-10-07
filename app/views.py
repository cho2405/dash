# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.template import loader
from django.http import HttpResponse
from django import template
from django.db.models import Count
from django.core import serializers
from django.template.loader import render_to_string
from django.http import JsonResponse
    
from .models import Trading

@login_required(login_url="/login/")
def index(request):
    
    context = {}
    context['segment'] = 'index'

    html_template = loader.get_template( 'index.html' )
    return HttpResponse(html_template.render(context, request))


def load_geodata(file_name):
    import json
    
    with open(file_name) as json_file:
        json_data = json.load(json_file)
        return json.dumps(json_data)
        

def load_trades_json(set_month):
    import json
    import pandas as pd

    gu_trades = Trading.objects.values('GU_CODE','TRADE_MONTH').annotate(GU_TRADE_CNT=Count('TRADE_MONTH'))

    df = pd.DataFrame(list(gu_trades))
    df.drop_duplicates(["GU_CODE", "TRADE_MONTH"], inplace=True)
    
    df = df[df['TRADE_MONTH'] == set_month]
    df = df.pivot(index="GU_CODE", columns="TRADE_MONTH", values="GU_TRADE_CNT")    
    gu_json = df[set_month].to_json(orient="columns")
    print(gu_json)
    return gu_json


@login_required(login_url="/login/")
def maps(request, pg_num):
    data = dict()
    context = {}
    print('--------------')
    context['months'] = Trading.objects.values('TRADE_MONTH').distinct()
    print(context['months'])
    
    
    
    if request.method == 'GET':
        set_month = pg_num
        print('GET')
        print(set_month)
        file_name = 'TL_SCCO_SIG.json'
        context['gu_json'] = load_trades_json(set_month)
        context['geo_json'] = load_geodata(file_name)
        
        html_template = loader.get_template( 'maps-jqvmap.html' )

        return HttpResponse(html_template.render(context, request))
        #return HttpResponse(render(request, 'maps-jqvmap.html', context))
    
    from django.forms.models import model_to_dict

    from django.core import serializers
    import json
    from django.core.serializers.json import DjangoJSONEncoder
    if request.method == 'POST':
        print("----")
        if 'search_gu_input' in request.POST:
            print( request.POST)
            search = request.POST.get('search_gu_input')
            gu_table = Trading.objects.filter(GU_CODE=search).values('GU_CODE','DONG_NAME', 'TRADE_DATE', 'APT_NAME', 'TRADE_PRICE')
            #context['results'] = serializers.serialize('json', str(list(gu_table)))
            context['results'] =  list(gu_table)
            #context['results'] = json.dumps(list(gu_table), cls=DjangoJSONEncoder)
            #context['results'] = json.dumps(list(gu_table)) 
            
            print('%%%%%')
            print(type(list(gu_table)))
            return JsonResponse(context)
        
        if 'search_month_input' in request.POST:
            file_name = 'TL_SCCO_SIG.json'
            context['gu_json'] = load_trades_json(set_month)
            context['geo_json'] = load_geodata(file_name)
            return JsonResponse(context)
        
    


@login_required(login_url="/login/")
def pages(request):
    context = {}
    # All resource paths end in .html.
    # Pick out the html file name from the url. And load that template.
    try:
        load_template      = request.path.split('/')[-1]
        context['segment'] = load_template
            
        html_template = loader.get_template( load_template )
        return HttpResponse(html_template.render(context, request))
        
    except template.TemplateDoesNotExist:

        html_template = loader.get_template( 'page-404.html' )
        return HttpResponse(html_template.render(context, request))
'''
    except:
    
        html_template = loader.get_template( 'page-500.html' )
        return HttpResponse(html_template.render(context, request))

'''
    
    
