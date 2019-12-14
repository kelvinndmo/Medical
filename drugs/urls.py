from django.urls import path

from drugs.views import ListCreateDrug, VerifyDrug,  CreatePharmacy

app_name = "authentication"

urlpatterns = [
    path('', ListCreateDrug.as_view(), name="login"),
    path('pharmacy', CreatePharmacy.as_view(), name="create pharmcy"),
    path('<drug_id>', VerifyDrug.as_view(), name="verify_drug")
]
