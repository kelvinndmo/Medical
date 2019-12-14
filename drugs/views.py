# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import uuid

from django.shortcuts import render


from rest_framework import generics
from rest_framework.response import Response

from drugs.serializers import DrugSerializer, PharmacySerializer
from drugs.models import Drugs, Pharmacy

from utils.permissions import IsPharmacistOrGO, ReadOnly, IsGovernmentAdmin
# Create your views here.


class ListCreateDrug(generics.ListCreateAPIView):
    serializer_class = DrugSerializer
    queryset = Drugs.objects.all()
    permission_classes = (IsPharmacistOrGO | ReadOnly,)

    def post(self, request):
        user = request.user
        drug = request.data
        print(user.role)

        serializer = self.serializer_class(data=drug)
        serializer.is_valid(raise_exception=True)
        serializer.save(drug_registerer=user, drug_id=str(uuid.uuid4())[:6])

        response = {
            "data": serializer.data,
            "message": "drug created successfully"
        }

        return Response(response)


class VerifyDrug(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = DrugSerializer
    queryset = Drugs.objects.all()

    def get(self, request, drug_id):
        user = request.user
        drug_data = request.data

        verifying_drug = Drugs.objects.get(drug_id=drug_id)
        if verifying_drug:
            serializer = self.get_serializer(verifying_drug)
            response = {
                "drug": serializer.data,
                "message": "This drug exists and it is from a verified manufucturer"
            }
            return Response(response)


class CreatePharmacy(generics.ListCreateAPIView):
    """ this is to enable CRUD actions of a pharmacy  """
    serializer_class = PharmacySerializer
    queryset = Pharmacy.objects.all()
    permission_classes = (IsGovernmentAdmin, )

    def post(self, request):
        user = request.user
        drug_data = request.data

        serializer = self.serializer_class(data=drug_data)
        serializer.is_valid(raise_exception=True)
        serializer.save(pharmacist=user)

        response = {
            "phamarcy": serializer.data,
            "message": "Phamrcy created successfully"
        }

        return Response(response)
