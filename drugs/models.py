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


class Manufucturer(models.Model):
    """ model class for class manufacturer """
    location = models.CharField(max_length=255)
    admin = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="manufucturer")
    registration_number = models.CharField(
        max_length=100, blank=True, unique=True)
    country = models.CharField(max_length=255)
    contact = models.CharField(max_length=255)


class Pharmacy(models.Model):
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    pharmacist = models.ForeignKey(
        User, max_length=255, on_delete=models.CASCADE, null=True)
