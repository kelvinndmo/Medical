from django.urls import path

from drugs.views import (ListCreateDrug, VerifyDrug,
                         CreatePharmacy, PharmacyRetrieveUpdateDestroyAPIView,
                         PharamcyRegisterForDrugs, GetPharamcies)

app_name = "authentication"

urlpatterns = [
    path('', ListCreateDrug.as_view(), name="login"),
    path('pharmacy/<pharmacist_id>',
         CreatePharmacy.as_view(), name="create pharmcy"),
    path('<drug_id>', VerifyDrug.as_view(), name="verify_drug"),
    path('pharmacy/<pharmacy_id>',
         PharmacyRetrieveUpdateDestroyAPIView.as_view(), name="pharamcy"),
    path('pharmacies/',
         GetPharamcies.as_view(), name="get-pharmacies"),
    path("add_drug/<pharmacy_id>/<drug_id>",
         PharamcyRegisterForDrugs.as_view(), name="register_drugs")
]
