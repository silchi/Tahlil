"""Tahlil URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconfs
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
# -*- coding: utf-8 -*-
from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'UI.views.show_home'),
    url(r'^home/$', 'UI.views.show_home'),
    url(r'^definition-tour/$', 'Creation.views.definition_tour'),
    url(r'^show-tour/$', 'Market.views.show_tour'),
    url(r'^profile/$', 'Dashboard.views.show_profile'),
    url(r'^domestic/$', 'Market.views.show_domestic'),
    url(r'^international/$', 'Market.views.show_international'),
    url(r'^hotels/$', 'Market.views.show_hotels'),
    url(r'^restaurants/$', 'Market.views.show_restaurants'),
    url(r'^transportation/$', 'Market.views.show_transportation'),
    url(r'^register-tourist/$', 'Register.views.show_register_tourist'),
    url(r'^register-agency/$', 'Register.views.show_register_agency'),
    url(r'^login/$', 'Register.views.do_login'),
    url(r'^logout/$', 'Register.views.do_logout'),
    url(r'^cancel/(?P<ticket_id>[0-9]+)/$', 'Dashboard.views.cancel', name='cancel'),
    url(r'^confirm/(?P<ticket_id>[0-9]+)/$', 'Dashboard.views.confirm', name='confirm'),
    url(r'^cart/$', 'Financial.views.cart', name='cart'),
    url(r'^cart/cancel/(?P<ticket_id>[0-9]+)/$', 'Financial.views.cancel', name='cart-cancel'),
    url(r'^cart/confirm/(?P<ticket_id>[0-9]+)/$', 'Financial.views.confirm', name='cart-confirm'),
    url(r'^cart/reserve/(?P<ticket_id>[0-9]+)/$', 'Financial.views.reserve', name='cart-reserve'),
    url(r'^cart/buy/$', 'Financial.views.buy', name='cart-buy'),
]