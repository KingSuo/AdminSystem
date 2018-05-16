#!/usr/bin/env python3
# -*- coding: utf-8 -*- 

"""
@version: python3.5.2
@author: King Suo 
@contact: 2354917594@qq.com
@software: PyCharm
@file: urls.py
@time: 2018/5/16 下午5:36
"""

from django.conf.urls import url

from apps.BlueMoon import views


urlpatterns = [
    url(r'^index/$', views.IndexView.as_view(), name='index'),
    url(r'^index2/$', views.Index2View.as_view(), name='index2'),
    url(r'^forms/$', views.FormsView.as_view(), name='forms'),
    url(r'^flot/$', views.FlotView.as_view(), name='flot'),
    url(r'^graphs/$', views.GraphsView.as_view(), name='graphs'),
    url(r'^vector-maps/$', views.VectorMapsView.as_view(), name='vector-maps'),
    url(r'^ui-elements/$', views.UiElementsView.as_view(), name='ui-elements'),
    url(r'^panels/$', views.PanelsView.as_view(), name='panels'),
    url(r'^notifications/$', views.NotificationsView.as_view(), name='notifications'),
    url(r'^icons/$', views.IconsView.as_view(), name='icons'),
    url(r'^blog/$', views.BlogView.as_view(), name='blog'),
    url(r'^blog-full-page/$', views.BlogFullPageView.as_view(), name='blog-full-page'),
    url(r'^edit-profile/$', views.EditProfileView.as_view(), name='edit-profile'),
    url(r'^invoice/$', views.InvoiceView.as_view(), name='invoice'),
    url(r'^default/$', views.DefaultView.as_view(), name='default'),
    url(r'^login/$', views.LoginView.as_view(), name='login'),
    url(r'^help/$', views.HelpView.as_view(), name='help'),
    url(r'^404/$', views.Err404View.as_view(), name='404'),
    url(r'^500/$', views.Err500View.as_view(), name='500'),
    url(r'^tables/$', views.TablesView.as_view(), name='tables'),
    url(r'^pricing/$', views.PricingView.as_view(), name='pricing'),
    url(r'^timeline/$', views.TimelineView.as_view(), name='timeline'),
    url(r'^media/$', views.MediaView.as_view(), name='media'),
    url(r'^calendar/$', views.CalendarView.as_view(), name='calendar'),
    url(r'^typography/$', views.TypographyView.as_view(), name='typography'),
]
