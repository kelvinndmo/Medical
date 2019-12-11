from django.urls import path

from drugs.views import ListCreateDrug

app_name = "authentication"

urlpatterns = [
    path('', ListCreateDrug.as_view(), name="login"),
]
