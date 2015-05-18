#!/usr/bin/env python
# coding: utf-8

from django.template.response import TemplateResponse
from screw.settings import mongo_client

SCREW_DB = mongo_client.screw


def index(request, template):
    goods = SCREW_DB.goods.find()
    return TemplateResponse(request, template, {'entry': goods})
