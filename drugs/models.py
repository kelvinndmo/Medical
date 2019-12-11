# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import uuid

from django.db import models
from utils.models import BaseAbstractModel
from authentication.models import User

# Create your models here.


class Drugs(models.Model):
    """model class for our drugs """


    drug_name = models.CharField(max_length=255)
    drug_id = models.CharField(
        max_length=100, blank=True, unique=True)
    manufucturer = models.CharField(max_length=255)
    serial_number = models.CharField(max_length=255)
    drug_registerer = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="drug_registerer")
    drug_verification = models.BooleanField(default=False)
