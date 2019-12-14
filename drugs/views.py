# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import uuid

from django.shortcuts import render, get_object_or_404


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

    def get(self, request, drug_id):
        user = request.user
        drug_data = request.data

        verifying_drug = get_object_or_404(Drugs, drug_id=drug_id)
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
    permission_classes = (IsGovernmentAdmin | ReadOnly, )

    def post(self, request):
        user = request.user
        drug_data = request.data

        serializer = self.serializer_class(data=drug_data)
        print("*********")
        serializer.is_valid(raise_exception=True)
        serializer.save(pharmacist=user, pharmacy_id=str(uuid.uuid4())[:10])

        response = {
            "phamarcy": serializer.data,
            "message": "Phamrcy created successfully"
        }

        return Response(response)


class PharmacyRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = PharmacySerializer

    def get(self, request, pharmacy_id):
        user = request.user

        veryfying_pharmacy = get_object_or_404(
            Pharmacy, pharmacy_id=pharmacy_id)
        serializer = self.get_serializer(veryfying_pharmacy)
        response = {
            "data": serializer.data,
            "message": "Pharmacy verified successfully..."
        }
        return Response(response)


class PharamcyRegisterForDrugs(generics.CreateAPIView):
    serializer_class = PharmacySerializer

    def post(self, request, pharmacy_id, drug_id):

        drug = get_object_or_404(Drugs, drug_id=drug_id)
        pharmacy = get_object_or_404(Pharmacy, pharmacy_id=pharmacy_id)

        pharmacy.drugs.add(drug)

        response = {
            "message": "drug added successfully to the store"
        }

        return Response(response)
