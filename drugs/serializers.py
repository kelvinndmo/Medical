from rest_framework import serializers
from drugs.models import Drugs


class DrugSerializer(serializers.ModelSerializer):
    class Meta:
        model = Drugs
        fields = ['drug_name', 'drug_id', 'manufucturer',
                  'serial_number', 'drug_verification']
