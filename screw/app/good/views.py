#!/usr/bin/env python
# coding: utf-8

from django.views.generic import View
from django.template.response import TemplateResponse
from screw.settings import mongo_client
from bson import ObjectId

SCREW_DB = mongo_client.screw


class GoodCreate(View):

    def get(self, request, template):
        gid = request.GET.get('gid')
        good = dict()
        if gid:
            assert(isinstance(gid, ObjectId))
            good = SCREW_DB.goods.find_one({'_id': gid})

        return TemplateResponse(request, template, {'entry': good})
