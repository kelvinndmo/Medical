# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from drugs.models import Drugs, Pharmacy

admin.site.register(Drugs)
admin.site.register(Pharmacy)

# Register your models here.
