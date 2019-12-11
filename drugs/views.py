# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import uuid

from django.shortcuts import render

from rest_framework import generics
from rest_framework.response import Response

from drugs.serializers import DrugSerializer
from drugs.models import Drugs

# Create your views here.


class ListCreateDrug(generics.ListCreateAPIView):
    serializer_class = DrugSerializer
    queryset = Drugs.objects.all()

    def post(self, request):
        user = request.user
        drug = request.data
        print(user)

        serializer = self.serializer_class(data=drug)
        serializer.is_valid(raise_exception=True)
        serializer.save(drug_registerer=user, drug_id=str(uuid.uuid4())[:6])

        response = {
            "data": serializer.data,
            "message": "drug created successfully"
        }

        return Response(response)
