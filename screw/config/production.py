#!/usr/bin/env python
# encoding: utf-8

# Django settings for screw project.

DEBUG = True

MONGODB_HOST = '127.0.0.1:27017'
MONGODB_NAME = 'screw'
MONGODB_DATABASE_HOST = 'mongodb://%s/%s' % (MONGODB_HOST, MONGODB_NAME)
