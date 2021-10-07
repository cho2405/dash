# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.urls import path, re_path
from app import views
from django.conf.urls import url, include
app_name = "app"
urlpatterns = [

    # The home page
    path('', views.index, name='home'),
    
    # Matches any html file
    
    path('maps-jqvmap/<int:pg_num>', views.maps, name='maps_url'),
    
    #path('maps-jqvmap', views.maps, name='maps'),
    #url(r'^maps-jqvmap/<int:pg_num>', views.maps, name='maps'),
    re_path(r'^.*\.*', views.pages, name='pages'),

]
