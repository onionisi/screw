#!/usr/bin/env python
# coding: utf-8

from django.conf.urls import patterns, url
from screw.app.good.views import GoodCreate, GoodDetail


urlpatterns = patterns(
    '',
    url(r'^good_upload/$', GoodCreate.as_view(),
        {'template': 'good/good_edit.html'}, name='good-upload'),
    url(r'^good_detail/$', GoodDetail.as_view(),
        {'template': 'good/good_detail.html'}, name='good-detail'),
)
