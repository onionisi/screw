from django import template
from screw.settings import STATIC_URL


register = template.Library()


@register.filter
def get_goods_pic_path(filename):
    return '%simages/goods/%s'% (STATIC_URL, filename)

@register.filter
def get_pymongo_document_id(document):
    return document.get('_id', '')
