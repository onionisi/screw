#!/usr/bin/env python
# coding: utf-8

from django.views.generic import View
from django.template.response import TemplateResponse
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from screw.settings import mongo_client, STATIC_URL, IMAGE_PATH
from bson import ObjectId
from PIL import Image
import uuid
import tempfile

SCREW_DB = mongo_client.screw


class GoodCreate(View):

    def get(self, request, template):
        gid = request.GET.get('gid')
        good = dict()
        if gid:
            assert(isinstance(gid, ObjectId))
            good = SCREW_DB.goods.find_one({'_id': gid})

        return TemplateResponse(request, template, {'entry': good})

    def post(self, request, template):
        good_keys = ['catalog', 'name', 'subname', 'price', 'discount']
        good = dict()
        gid = request.POST.get('gid')
        if gid:
            good = SCREW_DB.goods.find_one({'_id':gid})
        for key in good_keys:
            good[key] = request.POST.get(key)

        if gid:
            SCREW_DB.goods.save(good)
        else:
            gid = 'G'+(str(uuid.uuid4()).split('-'))[4].upper()

            send_file = request.FILES['pic']
            tmp_file = tempfile.NamedTemporaryFile(delete=True)
            for chunk in send_file.chunks():
                tmp_file.write(chunk)
            tmp_file.seek(0)

            try:
                im = Image.open(tmp_file.name)
            except IOError:
                tmp_file.close()
                raise IOError

            # saving two type
            image_path = IMAGE_PATH + "goods/"
            image_format = 'jpg'
            name_174 = gid + '_174.' + image_format
            thumbnail_174 = image_path + name_174
            im.thumbnail((174, 174), Image.ANTIALIAS)
            im.save(str(thumbnail_174), 'JPEG')

            name_94 = gid + '_94.' + image_format
            thumbnail_94 = image_path + name_94
            im.thumbnail((94, 94), Image.ANTIALIAS)
            im.save(str(thumbnail_94), 'JPEG')

            # close temp
            tmp_file.close()

            good['_id'] = gid
            good['image1'] = name_174
            good['image2'] = name_94

            SCREW_DB.goods.insert(good)

        return HttpResponseRedirect(reverse('good-upload'))


class GoodDetail(View):

    def get(self, request, template):
        gid = request.GET.get('goods_id')
        entry = SCREW_DB.goods.find_one({'_id':gid})
        return TemplateResponse(request, template, {'entry': entry})
